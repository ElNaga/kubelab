const express = require('express');
const mongoose = require('mongoose');


const app = express();
app.use(express.json());

const init = () => {
    // const dsn = 'mongodb://172.17.0.1:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false';
    const dsn = 'mongodb://mongo:27017/test';
    mongoose.connect (
    dsn,
    err => {
        if (err) return console.log(err);
        console.log('Connected to DB!')
    }
);}

// sudo docker run -d -p 27017:27017 mongo - docker command for init


init();
const Movie = mongoose.model(
    'movie',
    {
        "name": String,
        "year": String
    },
    'movie'
);

const create = async (data) => {
    let m = new Movie(data);
    console.log(data)
    return m.save();
};

const getAll = async () => {
    console.log('this is getAll fucntion')
    return Movie.find()
}

const findAll = async (req, res) => {
    try {
        let data = await getAll();
        res.send(data).status(200);
    } catch (err) {
        console.log(err);
        res.send('Internal Server Error').status(500);
    }
}

let Movie1 = {
    name: 'Bla',
    year: '222'
}

create(Movie1)

app.get('/', (req, res) => {

    res.send('Hello World!');
})

app.get('/movie',  findAll)

app.listen(10000, ()=> {
    console.log('App is running on port 1000!');
})
.on('error', (err) => {
    console.log(err);
})