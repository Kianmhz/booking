const jwt = require('jsonwebtoken');

const authenticate = (req, res, next) => {
    const token = req.header('Authorization');
    if (!token) return res.status(401).send('Access Denied');

    try {
        const verified = jwt.verify(token, 'your_secret_key');
        req.user = verified;
        next();
    } catch (err) {
        res.status(400).send('Invalid Token');
    }
};

const authorize = (role) => (req, res, next) => {
    if (req.user.role !== role) return res.status(403).send('Access Forbidden');
    next();
};

module.exports = { authenticate, authorize };
