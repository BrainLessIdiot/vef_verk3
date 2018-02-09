<!DOCTYPE html>
    <html>
    <head>
        <title>{{title}}</title>
        <meta charset="utf-8">
        <link type="text/css" href="/css/styles.css" rel="stylesheet">


    </head>
    <body>
        % frettir = ["Björn étur konu", "Maðurinn er Glaður","björn@tskoli.is"]
        <h2>{{frettir[0]}}</h2>
        <h3>{{frettir[1]}}</h3>
        <h4><b><i>{{frettir[2]}}</i></b></h3>

        %samlagning = 0
        %for X in kt
        <h1>Nú er Leyðinlegt</h1>
        %for i in range(10):
        <h1>Númer {{1}}</h1>
        %end
       <li><a href="/frettir">Björn borðar konu</a></li>
        <li><a href="/ken">kennitala</a></li>
        <li><a href="/pic">Steve Jobs saga</a></li>


    </body>
    </html>
