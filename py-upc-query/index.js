var exec = require('child_process').spawn;

exports.handler = function(event,context){
    console.log(event)
    const child = spawn('env/bin/python', ["run.py", event]);

    child.stdout.on('data', (data) => {
        return data
    });
}