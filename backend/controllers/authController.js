const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const db = require('../services/db');

const login = async (req, res) => {
    const { email, password } = req.body;
    try {
        const [user] = await db.query('SELECT * FROM users WHERE email = ?', [email]);
        if (user.length === 0) return res.status(404).send('User not found');

        const isMatch = await bcrypt.compare(password, user[0].password);
        if (!isMatch) return res.status(401).send('Invalid credentials');

        const token = jwt.sign({ id: user[0].id, role: user[0].role }, 'your_secret_key', { expiresIn: '1h' });
        res.json({ token });
    } catch (err) {
        res.status(500).send('Server error');
    }
};

const logout = (req, res) => {
    req.session.destroy((err) => {
        if (err) return res.status(500).send('Error logging out');
        res.send('Logged out successfully');
    });
};

module.exports = { login, logout };
