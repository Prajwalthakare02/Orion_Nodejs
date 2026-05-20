// Custom Gateway Authentication Checking Middleware
export const checkAuthentication = (req, res, next) => {
    // Extract token string from the custom request headers
    const authToken = req.headers['x-auth-token'];

    if (!authToken) {
        console.log(` -> [Security Gateway Exception]: Denied access. Auth Token parameter missing.`);
        return res.status(401).json({ error: "Access Denied: Missing mandatory authentication token in header 'x-auth-token'." });
    }

    // Simulate basic validation check (In production, this would verify a JWT signature)
    if (authToken !== 'prajwal_secure_secret_token') {
        console.log(` -> [Security Gateway Exception]: Denied access. Invalid Token context.`);
        return res.status(403).json({ error: "Access Forbidden: Provided authentication payload is invalid or expired." });
    }

    console.log(` -> [Security Gateway Success]: Identity authenticated successfully.`);
    
    // Credentials verified. Advance downstream to the next application handler execution block
    next();
};