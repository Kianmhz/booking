const mysql = require('mysql2');

const pool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: '12345',
    database: 'airbnbrental',
});


// Test the connection
pool.query('SELECT 1 + 1 AS solution', (err, results) => {
    if (err) {
        console.error('Error connecting to the database:', err.message);
    } else {
        console.log('Database connection successful. Query result:', results);
    }
});
