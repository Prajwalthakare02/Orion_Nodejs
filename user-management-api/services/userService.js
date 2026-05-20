const { randomUUID } = require('crypto');
const users = require('../data/users');

class UserService {
    getAllUsers() {
        return users;
    }

    getUserById(id) {
        return users.find(u => u.id === id);
    }

    createUser(data) {
        const newUser = { id: randomUUID(), ...data };
        users.push(newUser);
        return newUser;
    }

    updateUser(id, data) {
        const index = users.findIndex(u => u.id === id);
        if (index === -1) return null;
        users[index] = { ...users[index], ...data };
        return users[index];
    }

    deleteUser(id) {
        const index = users.findIndex(u => u.id === id);
        if (index === -1) return false;
        users.splice(index, 1);
        return true;
    }
}

module.exports = new UserService();