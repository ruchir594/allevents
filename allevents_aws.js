'use strict';

// Getting started with Facebook Messaging Platform
// https://developers.facebook.com/docs/messenger-platform/quickstart

const express = require('express');
//const request = require('superagent');
const bodyParser = require('body-parser');
const http = require('http');

var spawn = require("child_process").spawn;
var PythonShell = require('python-shell');

// Variables
//let pageToken = "";
let pageToken = "EAAJffei4MlEBAAsOcdoRvIXuvZADZAIpCDqEozNZB5OcyKZBZCCn4yWU7lCLut0hGyZCHpNBjVohXbE8TwunqnwZA1nWivurifm9iMVyM74pNJvwg0WC9UriuJABn0crPMvyRm6sFzI8BfWeQ8nXWDiyJgPs4qw2fP84N7JEuE9FwZDZD";
const verifyToken = "newton";

const app = express();
const fs = require('fs');

app.use(bodyParser.json());

app.get('/webhook', (req, res) => {
    if (req.query['hub.verify_token'] === verifyToken) {
        return res.send(req.query['hub.challenge']);
    }
    res.send('Error, wrong validation token');
    console.log(req.query);
    console.log(req.query.message);
    console.log(req.query.userid);
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

            res.send('Received POST request on /webhook successfully.');

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

 http.createServer(app).listen(80, function () {
  console.log('App is running on port 80');
});
