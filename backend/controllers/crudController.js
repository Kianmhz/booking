const db = require('../services/db');
const bcrypt = require('bcryptjs');

const createUser = async (req, res) => {
    const { name, email, password } = req.body;
    try {
        const hashedPassword = await bcrypt.hash(password, 10);
        await db.query('INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)', [name, email, hashedPassword, 'user']);
        res.send('User created');
    } catch (err) {
        res.status(500).send('Database error');
    }
};

const getUsers = async (req, res) => {
    try {
        const [users] = await db.query('SELECT * FROM users');
        res.json(users);
    } catch (err) {
        res.status(500).send('Database error');
    }
};

module.exports = { createUser, getUsers };
