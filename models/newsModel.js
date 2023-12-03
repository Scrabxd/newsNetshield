const sequelize = require('sequelize')
const {STRING, INTEGER} = require('sequelize')


const db = new sequelize(
    'aexjcmyn',
    'aexjcmyn',
    'QlHahIT_R8Bi4CDHuiiRYMFj7t0MVkHF',
    {
    host:"batyr.db.elephantsql.com",
    dialect:'postgres'
})


const News = db.define('news',{
    id:{
        type:INTEGER,
        primaryKey: true,
        allowNull:false,
        autoIncrement:true
    },
    title:{
        type:STRING
    },
    description:{
        type:STRING
    },
    image_url:{
        type:STRING
    },
    link:{
        type:STRING
    }
},{
    freezeTableName:true,
    timestamps:false
})

module.exports = News