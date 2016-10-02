'use strict';

// Getting started with Facebook Messaging Platform
// https://developers.facebook.com/docs/messenger-platform/quickstart

const express = require('express');
const request = require('superagent');
var request2 = require('request');
const bodyParser = require('body-parser');
const https = require('https');
var http = require("http");

var spawn = require("child_process").spawn;
var PythonShell = require('python-shell');

// Variables
//let pageToken = "";
let pageToken = "EAAJffei4MlEBAAsOcdoRvIXuvZADZAIpCDqEozNZB5OcyKZBZCCn4yWU7lCLut0hGyZCHpNBjVohXbE8TwunqnwZA1nWivurifm9iMVyM74pNJvwg0WC9UriuJABn0crPMvyRm6sFzI8BfWeQ8nXWDiyJgPs4qw2fP84N7JEuE9FwZDZD";
const verifyToken = "newtonIsTheGreatestManEverLived";
const privkey = "/etc/letsencrypt/live/yelper.tonatasha.com/privkey.pem";
const cert = "/etc/letsencrypt/live/yelper.tonatasha.com/cert.pem";
const chain = "/etc/letsencrypt/live/yelper.tonatasha.com/chain.pem";

const app = express();
const fs = require('fs');

app.use(bodyParser.json());

app.get('/webhook', (req, res) => {
    if (req.query['hub.verify_token'] === verifyToken) {
        return res.send(req.query['hub.challenge']);
    }
    res.send('Error, wrong validation token');
});
app.post('/webhook', (req, res) => {
    const messagingEvents = req.body.entry[0].messaging;

    messagingEvents.forEach((event) => {
        const sender = event.sender.id;

        if (event.postback) {
            const text = JSON.stringify(event.postback).substring(0, 200);
            //sendTextMessage(sender, 'Postback received: ' + text);
        } else if (event.message && event.message.text) { // bracket 101 open
            const text = event.message.text.trim().substring(0, 200);
            var request = require('request');

            var propertiesObject = { message: text, userid: sender };
            var aws_url = 'http://ec2-54-191-44-236.us-west-2.compute.amazonaws.com/webhook'
            console.log('sender: ',sender, 'message: ', text)
            request2({url:aws_url, qs:propertiesObject}, function(err, response, body) {
              if(err) { console.log(err); return; }
              console.log("Get response: " + response.statusCode);
              console.log("Get response: " + response.body);
              console.log(response.body['userid'], response.body['response'])
            });


        } //bracket 101 close
    });

    res.sendStatus(200);
});

app.post('/token', (req, res) => {
    if (req.body.verifyToken === verifyToken) {
        pageToken = req.body.token;
        return res.sendStatus(200);
    }
    res.sendStatus(403);
});
app.get('/token', (req, res) => {
    if (req.body.verifyToken === verifyToken) {
        return res.send({token: pageToken});
    }
    res.sendStatus(403);
});

 https.createServer({
      key: fs.readFileSync(privkey),
      cert: fs.readFileSync(cert),
      ca: fs.readFileSync(chain)
    }, app).listen(3600, function () {
  console.log('App is running on port 3600');
});

function sendMessage (sender, message) {
    request
        .post('https://graph.facebook.com/v2.6/me/messages')
        .query({access_token: pageToken})
        .send({
            recipient: {
                id: sender
            },
            message: message
        })
        .end((err, res) => {
            if (err) {
                console.log('Error sending message: ', err);
            } else if (res.body.error) {
                console.log('Error: ', res.body.error);
            }
        });
}

function sendTextMessage (sender, text) {
    sendMessage(sender, {
        text: text
    });
}
