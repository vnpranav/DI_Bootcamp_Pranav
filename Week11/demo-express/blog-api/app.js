const express = require('express')
const app = express()
const posts = require("./data.js")

app.listen(3000, () => {
    console.log('server is listening on port 3000')
})

app.get('/api/posts', (req, res) => res.json(posts))
app.get('/api/posts/:postId', (req, res) => {
const pId = Number(req.params.postId)
const post = posts.find((p) => ( p.id === pId))

if (!post) {
    res.send("not found")
}

res.json(post)
})
