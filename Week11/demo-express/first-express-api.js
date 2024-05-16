const express = require('express')
const app = express()

app.listen(3000, () => {
    console.log('server is listening on port 5000')
})


app.get('/', (req, res) => res.send('Hello World!'))
app.get('/aboutme', (req, res) => res.send('I love coding!'))
app.get('/tutorial', (req, res) => res.send('Tutorial about express!'))
