// Custom Structural Content Validation Middleware
export const validateTaskTitle = (req, res, next) => {
    const { title } = req.body;

    // Reject processing if parameter is absent, non-string, or blank space
    if (!title || typeof title !== 'string' || title.trim() === '') {
        console.log(` -> [Schema Validation Failure]: Request discarded due to missing required 'title' field.`);
        return res.status(400).json({ error: "Data Validation Failure: The payload property 'title' is mandatory and must contain text content." });
    }

    // Sanitize data string input before parsing onwards
    req.body.title = title.trim();
    
    // Validation constraints satisfied. Advance downstream safely.
    next();
};