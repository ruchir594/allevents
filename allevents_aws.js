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
    //res.send('Error, wrong validation token');
    console.log(req.query);
    console.log(req.query.message);
    console.log(req.query.userid);

    /////////////////////////////////////////////////////////////////////////////////////////

            var d1 = [];
            d1.push('i', 'live', 'in', 'please', 'hi', 'give', 'find', 'who', 'what', 'my', 'hungry', 'near', 'me', 'thank', 'you');
            d1.push('want', 'to', 'eat', 'like','liked', 'I', 'can', 'you', 'suggest', 'of', 'is', 'are', 'near', 'there', 'some');
            d1.push('little', 'now', 'wanna', 'want', 'at', 'on', 'in', 'near', 'area', 'next', 'and', 'how', 'about', 'or');
            d1.push('the', 'a', 'an', 'about', 'for', 'with', 'should', 'could', 'would', 'out','time','person','year','way','day');
            d1.push('thing','man','world','life','hand','part','child','eye','woman','place','work','week', 'doing');
            d1.push('case','point','government','company','number','group','problem','fact','be','have','do','say');
            d1.push('get','make','go','know','take','see','come','think','look','want','give','use','find','tell', 'telling');
            d1.push('ask','work','seem','feel','try','leave','call','good','new','first','last','long','great','little','own','other');
            d1.push('old','right','big','high','different','small','large','next','early','young','important','few');
            d1.push('public','bad','same','able','to','of','in','for','on','with','at','by','from','up','about','into');
            d1.push('over','after','beneath','under','above','the','and','a','that','I','it','not','he','as','you');
            d1.push('this','but','his','they','her','she','or','an','will','my','one','all','would','there','their', 'talk');
            d1.push('talking', 'love', 'loved', 'hello', 'help', 'helping', 'helped', 'pleasure', 'bye', 'goodbye', 'care', 'later');
            d1.push('no','nothing', 'thanks', 'welcome', 'something', 'smart', 'dumb', 'poor', 'am', 'hey', 'bae', 'bea', 'no', 'okay', 'bye', 'ok', 'cool');
            d1.push('natasha');

            var text = req.query.message
            var sender = req.query.userid

            var text2 = text.replace(/\?/g,'');
            text2 = text2.replace(/!/g,'');
            text2 = text2.replace(/\./g,'');
            text2 = text2.replace(/,/g,'');
            text2 = text2.replace(/:/g,'');

            console.log("Receive a message2: " + text2);

            var words_text = text2.split(' ');

            var i = 0
            var flag = false
            var hasher = -1
            while(i<words_text.length){
              hasher = d1.indexOf(words_text[i].toLowerCase())
              if(hasher == -1){
                flag = true
                console.log("Flag true on: " + words_text[i]);
              }
              i = i + 1
            }
            if(flag == false){

              if(words_text[0].toLowerCase() == 'hi' || words_text[0].toLowerCase() == 'hello' || words_text[0].toLowerCase() == 'hey'){
                res.send({userid:sender, response:{text: "Hello, I am Hey Bae."}})
              }
              else if(words_text[0].toLowerCase() == 'who'){
                res.send({userid:sender, response:{text: "Hi there, I am a smart AI."}})
              }
              else if(words_text[0].toLowerCase() == 'what'){
                res.send({userid:sender, response:{text: "I help you find events near you using allevents.in, just tell me your city/area by typing below and pick an event from broad category allevents.in has to offer."}})
                //res.send({userid:sender, response:{text: "Meanwhile, please please like my page.")
              }
              else if(words_text[0].toLowerCase() == 'how'){
                res.send({userid:sender, response:{text: "Let's just say I am smart..."}})
                //res.send({userid:sender, response:{text: "Meanwhile, please please like my page.")
              }
              else if(words_text[0].toLowerCase() == 'goodbye' || words_text.indexOf('bye') != -1){
                res.send({userid:sender, response:{text: "Bye, thank you for dropping by."}})
                //res.send({userid:sender, response:{text: "Meanwhile, please please like my page.")
              }
              else if(words_text[0].toLowerCase() == 'thank' || words_text[0].toLowerCase() == 'thanks'){
                res.send({userid:sender, response:{text: "You are welcome."}})
                res.send({userid:sender, response:{text: "Meanwhile, please please like my page."}})
              }
              else if(words_text[0].toLowerCase() == 'you'){
                res.send({userid:sender, response:{text: "Well, you have strong opinions about me."}})
                //res.send({userid:sender, response:{text: "Meanwhile, please please like my page.")
              }
              else if(words_text[0].toLowerCase() == 'i' && words_text[1].toLowerCase() == 'want'){
                res.send({userid:sender, response:{text: "I cannot tell what you want, please be more specific and give me your location as well."}})
              }
              else if(words_text[0].toLowerCase() == 'i' && words_text[1].toLowerCase() == 'am'){
                res.send({userid:sender, response:{text: "Sure, you are! But I can suggest events near you using allevents.in if you tell me your city/are and what type of event you are looking for."}})
                //res.send({userid:sender, response:{text: "Meanwhile, please please like my page.")
              }
              else if(words_text[0].toLowerCase() == 'i'){
                res.send({userid:sender, response:{text: "Okay, maybe! But I can suggest events near you using allevents.in if you tell me your city/are and what type of event you are looking for."}})
              }
              else if(words_text[0].toLowerCase() == 'cool'){
                res.send({userid:sender, response:{text: "Cool!"}})
              }
              else if(words_text[0].toLowerCase() == 'ok' || words_text[0].toLowerCase() == "okay"){
                res.send({userid:sender, response:{text: "Have a nice day!"}})
              }
              else {
                res.send({userid:sender, response:{text: "hmmm... I can't tell your location. Tell me your city."}})
                //res.send({userid:sender, response:{text: "Meanwhile, please please like my page.")
              }

              //res.send({userid:sender, response:{text: "Nothing to Process...")


            } else { //bracket 102 open
              //res.send({userid:sender, response:{text: "processing...")

              //res.send({userid:sender, response:{text: 'Text received, so gtfo?: ' + text);
              var options = {
                mode: 'text',
                args: [text, sender]
              };
              PythonShell.run("./lambda_function.py" , options,function (err, results) {
                if (err) throw err;
                //console.log('result: %j', results);
                console.log('back in app.js')
                var results = String(results)
                console.log(results)
                var places = results.split("^");
                console.log(places)
                if (places[0] == 'jankiap50') {
                    res.send({userid:sender, response:{text:places[1]}});
                    //res.send({userid:sender, response:{text: "Hmmm something is wrong. I will report it, meanwhile, try searching something else?")
                    //res.send({userid:sender, response:{text: places[2]);
                    //res.send({userid:sender, response:{text: places[3])
                }
                else {
                  //res.send({userid:sender, response:{text: "Python shell ran successfully")
                  //res.send({userid:sender, response:{text: places[0])
                  //res.send({userid:sender, response:{text: String(places.length))
                  var aplace = [];
                  var aplacea="";
                  var i = 0;
                  var increment = 5;
                  while (i < places.length){
                      //aplacea = places[i]+"\n"+places[i+1]+"\n"+places[i+3]+"\n"+places[i+4];
                      aplace.push(places[i]+"^"+places[i+1]+"^"+places[i+2]+"^"+places[i+3]+"^"+places[i+4]);
                      if (typeof(places[i+1]) == typeof("hello")){
                      //res.send({userid:sender, response:{text: aplacea);
                      i=i+increment;
                      }
                      else {
                      i=i+increment;
                      }
                  }
                  //if (places[25] != ""){
                  //res.send({userid:sender, response:{text: places[25]);
                  //}
                  //res.send({userid:sender, response:{text: String(aplace.length));
                  res.send(sendGenericMessage(sender, aplace));
                  //res.send({userid:sender, response:{text: "Like the page? Share?.")
                }
              });
      } //bracket 102 close

});
app.post('/webhook', (req, res) => {
    const messagingEvents = req.body.entry[0].messaging;

    messagingEvents.forEach((event) => {
        const sender = event.sender.id;

        if (event.postback) {
            const text = JSON.stringify(event.postback).substring(0, 200);
            //res.send({userid:sender, response:{text: 'Postback received: ' + text);
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

function sendGenericMessage (sender, places) {
  if (places.length == 1)
    { //length == 1
      res.send({userid:sender, response:{text: "No event found."}});
  } // length == 1
  if (places.length == 2)
    { //length == 2
      //res.send({userid:sender, response:{text: "I am in two places.legth match");
    var textual0 = places[0].split('^')
    var textual1 = places[1].split('^')
      return({userid:sender, response:{
          attachment: {
            type: "template",
            payload: {
              template_type: "generic",
              elements: [{
                title: textual0[0],
                subtitle: textual0[1] + textual0[2],
                item_url: textual0[4],
                image_url: textual0[3],
                buttons: [{
                  type: "web_url",
                  url: textual0[4],
                  title: "See details"
                }],
              }]
            }
          }
      }});
  } // length == 2
  if (places.length == 3)
    { //length == 3
      //res.send({userid:sender, response:{text: "I am in three places.legth match");
    var textual0 = places[0].split('^')
    var textual1 = places[1].split('^')
    var textual2 = places[2].split('^')
      return({userid:sender, response:{
          attachment: {
            type: "template",
            payload: {
              template_type: "generic",
              elements: [{
                title: textual0[0],
                subtitle: textual0[1] + textual0[2],
                item_url: textual0[4],
                image_url: textual0[3],
                buttons: [{
                  type: "web_url",
                  url: textual0[4],
                  title: "See details"
                }],
              }, {
                title: textual1[0],
                subtitle: textual1[1] + textual1[2],
                item_url: textual1[4],
                image_url: textual1[3],
                buttons: [{
                  type: "web_url",
                  url: textual1[4],
                  title: "See details"
                }],
              }]
            }
          }
      }});
  } // length == 3
  if (places.length == 4)
    { //length == 4
      //res.send({userid:sender, response:{text: "I am in four places.legth match");
    var textual0 = places[0].split('^')
    var textual1 = places[1].split('^')
    var textual2 = places[2].split('^')
    var textual3 = places[3].split('^')
      return({userid:sender, response:{
          attachment: {
            type: "template",
            payload: {
              template_type: "generic",
              elements: [{
                title: textual0[0],
                subtitle: textual0[1] + textual0[2],
                item_url: textual0[4],
                image_url: textual0[3],
                buttons: [{
                  type: "web_url",
                  url: textual0[4],
                  title: "See details"
                }],
              }, {
                title: textual1[0],
                subtitle: textual1[1] + textual1[2],
                item_url: textual1[4],
                image_url: textual1[3],
                buttons: [{
                  type: "web_url",
                  url: textual1[4],
                  title: "See details"
                }],
              },{
                title: textual2[0],
                subtitle: textual2[1] + textual2[2],
                item_url: textual2[4],
                image_url: textual2[3],
                buttons: [{
                  type: "web_url",
                  url: textual2[4],
                  title: "See details"
                }],
              }]
            }
          }
      }});
  } // length == 4
  if (places.length == 5)
    { //length == 5
      //res.send({userid:sender, response:{text: "I am in five places.legth match");
    var textual0 = places[0].split('^')
    var textual1 = places[1].split('^')
    var textual2 = places[2].split('^')
    var textual3 = places[3].split('^')
    var textual4 = places[4].split('^')
      return({userid:sender, response:{
          attachment: {
            type: "template",
            payload: {
              template_type: "generic",
              elements: [{
                title: textual0[0],
                subtitle: textual0[1] + textual0[2], //+ textual0[2],
                item_url: textual0[4],
                image_url: textual0[3],
                buttons: [{
                  type: "web_url",
                  url: textual0[4],
                  title: "See details"
                }],
              }, {
                title: textual1[0],
                subtitle: textual1[1] + textual1[2],
                item_url: textual1[4],
                image_url: textual1[3],
                buttons: [{
                  type: "web_url",
                  url: textual1[4],
                  title: "See details"
                }],
              },{
                title: textual2[0],
                subtitle: textual2[1] + textual2[2],
                item_url: textual2[4],
                image_url: textual2[3],
                buttons: [{
                  type: "web_url",
                  url: textual2[4],
                  title: "See details"
                }],
              },{
                title: textual3[0],
                subtitle: textual3[1] + textual3[2],
                item_url: textual3[4],
                image_url: textual3[3],
                buttons: [{
                  type: "web_url",
                  url: textual3[4],
                  title: "See details"
                }],
              }]
            }
          }
      }});
  } // length == 5
}
