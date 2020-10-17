var express = require("express");
var app = express();
var bodyParser=require("body-parser");

app.use(bodyParser.urlencoded({extended:true}));

var photos=[{name:"baby1",url:"https://website-bamedag.netdna-ssl.com/fileadmin/media/_processed_/8/8/csm_7-9-months-introtext_fee7fcf815.jpg"},
{name:"baby2",url:"https://website-bamedag.netdna-ssl.com/fileadmin/media/_processed_/8/8/csm_7-9-months-introtext_fee7fcf815.jpg"}]

app.set("view engine","ejs");

app.get("/home",function(req,res)
{
    res.render('home');
});

app.get("/baby",function(req,res)
{
 res.render("hello",{babies:photos});

});

app.get("/baby/new",function(req,res)
{
    res.render("form");
});

app.post("/baby",function(req,res)
{
    res.redirect("/baby");
    var name = req.body.Title;
    var url = req.body.url;
    var newb={name:name,url:url};
    photos.push(newb);
 });
app.get("/baby/new")
app.listen(3000,function()
{
    console.log("we are live");
});