
        mapboxgl.accessToken = 'pk.eyJ1IjoiYWxpc29ucjIiLCJhIjoiY2ozMGc2cmJzMDAxMTJ3bjNtbGR5eGpnMyJ9.UvriR_RhUCjK72YOqAghUw';
        //Creates map. This is the only place where we pull from Mapbox——to get the style! You can use the generic mapbox styles (light and outdoors commented out below, but my custom map is just the outdoors one minus some of the place name layers to declutter)
        var map = new mapboxgl.Map({
            container: 'map',
            style: 'mapbox://styles/alisonr2/cj31orqf5000a2sqoehbxrfpe', //'mapbox://styles/mapbox/outdoors-v9',//mapbox://styles/mapbox/light-v9',
            center: [-75.1043514, 40.0264575, ], // starting position, the friends asylum!
            zoom: 5, // starting zoom
           
        });
  
       
        map.on('load', function(){ 
 
         //Adds the righthand zoom box:
        map.addControl(new mapboxgl.NavigationControl());
        //Makes a source called django-data which uses Django data in the GeoJSON Format. Be careful——any change of a comma, bracket, brace, or parentheses will screw up the GeoJSON format. 
        map.addSource("django-data", {
            "type": "geojson",
            "data": { "type" : "FeatureCollection",
            "features" : [{{places|safe}}, 
        }) //If this extra parenthese goes away, the whole map breaks. It looks like it's extra, but it closes the GeoJSON format. 
        
        //Creates a layer called QMH_Hometowns, populated by circles, whose source is the django-data from above and who is styled as specified below:
        map.addLayer({
        'id': 'QMH_Hometowns',
        'type': 'circle',
        "source": "django-data",
        //'source-layer': 'QMH_Hometowns',
         'paint': {
              'circle-opacity': 0.6,
            // Makes size proportional to # of people
            'circle-radius': {
                property:"Count",
                type:'categorical',
                stops:[
                    ['0', 0], ['1',8], ['2',9], ['3',10], ['4',11], ['5',12],['6',13], ['7',13], ['8',13], ['9', 14], ['10',14],
                    ['11',14], ['12',15], ['13',16], ['14', 17], ['15',18], ['16',19], ['17',20], ['18',21], ['19',22], ['20',23],
                    ['21',24], ['22',25],['23',26],['24',27],['25',28],['26',29],['27',30],['28',31],['29',32],['30',33],
                    ['31',34],['32',35],['33',36],['34',37],['35', 38],['36',39],['37',40],['38',41],['39',42], ['40', 43],
                    ['41', 44],
                    ['42', 45],
                    ['43', 45],
                    ['44', 45],
                    ['45', 45],
                    ['46', 45],
                    ['47', 45],
                    ['48', 45],
                    ['49', 45],
                    ['50', 45],
                    ['51', 45],
                    ['52', 45],
                    ['53', 45],
                    ['54', 45],
                    ['55', 45],
                    ['56', 45],
                    ['57', 45],
                    ['58', 45],
                    ['59', 45],
                    ['60', 45],
                    ['61', 45],
                    ['62', 45],
                    ['63', 45],
                    ['64', 45],
                    ['65', 45],
                    ['66', 45],
                    ['67', 45],
                    ['68', 45],
                    ['69', 45],
                    ['70', 45]
                        ]   
            },
            // Makes color correspond to # of people—darker orange/red = more (=bigger, from above)
             'circle-color':{
                 property:"Year",
                 type:'categorical',
                 stops: [
                    
                    ['1817', '#f7d5a1'],
                    ['1818', '#f7d5a1'],
                    ['1819', '#f5cc8e'],
                    ['1820', '#f5cc8e'],
                    ['1821', '#f4c47c'],
                    ['1822', '#f4c47c'],
                    ['1823', '#f2bb69'],
                    ['1824', '#f2bb69'],
                    ['1825', '#f0b356'],
                    ['1826', '#f0b356'],
                    ['1827', '#efaa43'],
                    ['1828', '#efaa43'],
                    ['1829', '#eda231'],
                    ['1830', '#eda231'],
                    ['1831', '#eb991e'],
                    ['1832', '#eb991e'],
                    ['1833', '#e18f14'],
                    ['1834', '#e18f14'],
                    ['1835', '#ce8312'],
                    ['1836', '#ce8312'],
                    ['1837', '#bc7710'],
                    ['1838', '#bc7710'],
                    ['1839', '#a96b0f'],
                    ['1840', '#a96b0f'],
                    ['1841', '#965f0d'],
                    ['1842', '#965f0d'],
                    ['1843', '#83530b'],
                    ['1844', '#83530b'],
                    ['1845', '#71470a'],
                    ['1846', '#71470a'],
                    ['1847', '#5e3c08'],
                    ['1848', '#5e3c08'],
                    ['1849', '#5e3c08'],
                    ['1850', '#4b3007'],
                    ['1851', '#4b3007'],
                    ['1852', '#4b3007'],
                    ['1853', '#382405'],
                    ['1854', '#382405'],
                    ['1855', '#382405'],
                    ['1856', '#261803']]
             },
            
            },
        }); //end of addLayer
      
        //Intializes map: start set at 1817, the early end of our slider/data.
        filterBy('1817')
        document.getElementById('slider').addEventListener('input', myFunction()); //Helps initialize
        }); //End of onLoad
        
        //Filters by the property Year; shows all points whose Year property is <= to the Year2 Parameter (taken from slider)
        function filterBy (Year2){
        var filters = ['<=', 'Year', Year2]; //for features in the QMH_Hometowns layer, show the ones for which the Year property <= the entered Year2.
        map.setFilter('QMH_Hometowns', filters); 
        }
         
        //Creates popups by mouse hover        
        var popup = new mapboxgl.Popup({
          closeButton: false,
            closeOnClick: false
        });
        map.on('mouseenter', 'QMH_Hometowns', function(e) {
          // Change the cursor style as a UI indicator.
          map.getCanvas().style.cursor = 'pointer';
          var to_Show = e.features[0].properties.Name +'<br>'+ e.features[0].properties.Year +'<br>'+e.features[0].properties.Count + " patients"
          if (e.features[0].properties.Count == 1){ //Just so that we never have the plural "1 patients" displayed. 
            var to_Show = e.features[0].properties.Name +'<br>'+e.features[0].properties.Year +'<br>'+ e.features[0].properties.Count + " patient"
          }
          popup.setLngLat(e.features[0].geometry.coordinates)
            .setHTML(to_Show)
            .addTo(map);
            });
        map.on('mouseleave', 'QMH_Hometowns', function() {
          map.getCanvas().style.cursor = '';
          popup.remove();
        });
          
       //A poorly-named but essential function which picks up which year the slider is set to and displays the year and filters by it.       
        function myFunction(){
            var x = document.getElementById("slider").value;
            
            console.log(x)
            document.getElementById("label").innerHTML = x;
            //document.getElementById("year-to-show").textContent = x;
            filterBy(x);
        }
 

