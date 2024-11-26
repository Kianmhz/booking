const express = require('express');
const { fetchWeather } = require('../controllers/apiController');

const router = express.Router();

router.get('/weather', fetchWeather);

module.exports = router;
