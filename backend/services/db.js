const mysql = require('mysql2');

const pool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: '12345',
    database: 'airbnbrental',
});

module.exports = pool.promise();
