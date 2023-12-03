const express = require('express')
const cors = require('cors')
const News = require('./models/newsModel')
const port = 4000;
const app = express()


app.use(cors())

app.get('/', async(req,res) => {
    return res.json({
        data: await News.findAll()
    })
})


app.listen(port,() => console.log(`App running in port ${port}`))