import express from 'express'
import * as r  from 'redis';
import dotenv from 'dotenv'
const app = express()

dotenv.config()
const counter = 0;
const redis = await r.createClient({
    host:'localhost',
    port:6379 
})
redis.connect()
const { PORT} = process.env;
await redis.set('vistis',0)

app.get('/',async(req,res)=>{
    const visits = await redis.get('visits', (err,value)=>{
        res.json({
            visits
        })
        redis.set('visits', Number(value)+1)
    })

}) 

app.listen(PORT,()=>{
    console.log(`Listening on port ${PORT}`)
})
