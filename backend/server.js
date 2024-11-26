const express = require('express');
const bodyParser = require('body-parser');
const session = require('express-session');
const errorHandler = require('./middleware/errorHandler');
const authRoutes = require('./routes/auth');
const crudRoutes = require('./routes/crud');
const apiRoutes = require('./routes/api');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use(session({
    secret: 'your_secret_key',
    resave: false,
    saveUninitialized: true,
}));

app.use('/auth', authRoutes);
app.use('/crud', crudRoutes);
app.use('/api', apiRoutes);

app.use(errorHandler);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
