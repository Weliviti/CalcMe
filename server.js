// server.js
const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Connect to MySQL
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'kaito1412', // replace with your MySQL password
    database: 'guess_game'
});

db.connect(err => {
    if (err) throw err;
    console.log("Connected to MySQL");
});

// API endpoint to save results
app.post('/save', (req, res) => {
    const { player, round, correct, totalTime } = req.body;
    const sql = 'INSERT INTO game_results (player_name, round, correct, total_time) VALUES (?, ?, ?, ?)';
    db.query(sql, [player, round, correct, totalTime], (err, result) => {
        if (err) return res.status(500).send(err);
        res.send({ success: true, id: result.insertId });
    });
});

// Start server
app.listen(3000, () => console.log("Server running on port 3000"));
