const userService = require('../services/userService');

class UserController {
    getAllUsers(req, res) {
        const users = userService.getAllUsers();
        res.status(200).json(users);
    }

    getUserById(req, res) {
        const user = userService.getUserById(req.params.id);
        if (!user) {
            return res.status(404).json({ message: 'User not found' });
        }
        res.status(200).json(user);
    }

    createUser(req, res) {
        const { name, email } = req.body;
        if (!name || !email) {
            return res.status(400).json({ message: 'Name and email are required' });
        }
        
        try {
            const newUser = userService.createUser({ name, email });
            res.status(201).json(newUser);
        } catch (error) {
            res.status(500).json({ message: 'Error creating user' });
        }
    }

    updateUser(req, res) {
        const updatedUser = userService.updateUser(req.params.id, req.body);
        if (!updatedUser) {
            return res.status(404).json({ message: 'User not found' });
        }
        res.status(200).json(updatedUser);
    }

    deleteUser(req, res) {
        const success = userService.deleteUser(req.params.id);
        if (!success) {
            return res.status(404).json({ message: 'User not found' });
        }
        res.status(204).send();
    }
}

module.exports = new UserController();