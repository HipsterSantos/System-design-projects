const express = require('express')
const redis = require('redis')

const app = express()
const client= redis.createClient({})
client.connect()// open redis connection
app.get('/',async(req,res)=>{
    await client.get('visits',(err,visits)=>{
        console.log('who visited was ', visits)
        client.set(visits)
        res.send(Number(visits))
    })
})
const port =  process.env.PORT || 8000
app.listen(port,console.log(`'listening on port ${port}'`))