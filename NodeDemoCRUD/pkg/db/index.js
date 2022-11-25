const mongoose = require('mongoose');

const init = () => {

    const dsn = "mongodb://localhost:27017/"

    // sudo docker run -d -p 27017:27017 mongo
    
    // const url = config.get('db').url
    // const password = config.get('db').password
    // const username = config.get('db').username
    // const dbName = config.get('db').dbName
    // const dsn = `mongodb+srv://${username}:${password}@${url}/${dbName}?retryWrites=true&w=majority`;

    mongoose.connect(
        dsn,
        err => {
            if(err) {
                return console.log('Could not connect to db', err);
            }
            console.log('Successfully connetcted to db');
        }
    )
};

module.exports = {
    init
};