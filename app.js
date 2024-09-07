const express = require('express')
const path = require('path')

const app = express();

// Middleware to render HTML files
app.engine('html', require('ejs').renderFile);  // Use EJS engine to render HTML

// Serve static files from the 'public' folder
app.use(express.static(path.join(__dirname, 'assets')));


// Routes for each page
app.get('/', (req, res) => {
    res.render('index.html');
});

app.get('/about', (req, res) => {
    res.render('about.html');
});

app.get('/chatbot', (req, res) => {
    res.render('chatbot.html');
});

app.get('/contact', (req, res) => {
    res.render('contact.html');
});

app.get('/facebooklogin', (req, res) => {
    res.render('facebooklogin.html');
});

app.get('/portfolio', (req, res) => {
    res.render('portfolio.html');
});

app.get('/ui-ux', (req, res) => {
    res.render('ui-ux.html');
});

app.get('/webdev', (req, res) => {
    res.render('webdev.html');
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});