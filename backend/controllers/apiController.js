const axios = require('axios');

const fetchWeather = async (req, res) => {
    try {
        const { city } = req.query;
        const response = await axios.get(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=your_api_key`);
        res.json(response.data);
    } catch (err) {
        res.status(500).send('API error');
    }
};

module.exports = { fetchWeather };
