const express = require('express');
const { createUser, getUsers } = require('../controllers/crudController');
const { authenticate, authorize } = require('../middleware/authMiddleware');

const router = express.Router();

router.post('/users', authenticate, authorize('admin'), createUser);
router.get('/users', authenticate, getUsers);

module.exports = router;
