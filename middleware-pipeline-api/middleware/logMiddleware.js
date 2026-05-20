// Custom Global Auditing Logger Middleware
export const requestLogger = (req, res, next) => {
    const timestamp = new Date().toISOString();
    const method = req.method;
    const url = req.url;
    
    console.log(`[Audit Log] [${timestamp}] Intercepted ${method} request matching pathway: ${url}`);
    
    // Crucial: Pass processing control down to the next middleware sequence line item
    next();
};