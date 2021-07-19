 $(window).load(function(){  
    var html = ''
    $.post("/rank_left",function(data){
        for(line in data){
            // html += data[line];
            html +='<li><p><span>'+line+'</span><span>'+data[line][0]+'</span><span>'+data[line][1]+'</span><span>'+data[line][2]+'</span></p></li>';
        }
        // alert(html);
        $('.rank_ul').html(html);
        $('.wrap,.adduser').liMarquee({
            direction: 'up',/*身上滚动*/
            runshort: false,/*内容不足时不滚动*/
            scrollamount: 20/*速度*/
        });
    });
    $.post("/chart1_json",function(data){
        var myChart = echarts.init(document.getElementById('chart1'));
        // alert(data['1']);
        myChart.setOption({
            title:{
                text:'周涨跌幅',
                textStyle:{
                    color:'rgba(255,255,255,.6)'
                }
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                    type: 'shadow',        // 默认为直线，可选为：'line' | 'shadow'
                    label:{
                        show:true
                    }
                }
            },
            dataZoom: [{
                show:true,
                start:0,
                end:20
            },{
                type: 'inside',
                start:0,
                end:20
            }],
            xAxis: {
                type: 'category',
                axisLabel:{
                    color:'rgba(255,255,255,.6)'
                },
                data:data['1']
            },
            yAxis: {
                type: 'value',
                axisLabel:{
                    color:'rgba(255,255,255,.6)'
                },
            },
            series:[{
                name:'涨跌幅',
                type:'bar',
                label:{
                    show:true,
                    formatter:'{b}',
                    color: 'rgba(10,9,9,0)',
                },
                itemStyle: {
                    color:'#49bcf7'
                },
                barGap:'30%',
                data:data['2']
            }]
        })
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    });
    $.post("/k_line_echart",{symbol:'BTC'}, function(data){
        var myChart = echarts.init(document.getElementById('k_line'));
                             
        // console.log(obj);
        var upColor = '#FF0000';
        var upBorderColor = '#8A0000';
        // var downColor = '#00da3c';
        var downColor ='#00FF00'
        var downBorderColor = '#008F28';
        var axisFontColor='#D8D8D8'
        // 得到选择框的数据
                                        
        // alert(data);        
        var data0 = splitData(data['1']);
        function splitData(rawData){
            var categoryData = [];
            var values =[]
            for( var line in rawData){
                categoryData.push(rawData[line].splice(0,1)[0]);
                values.push(rawData[line]);
            }
            return{
                categoryData:categoryData,
                values:values
            };
        };
                    
        function calculateMA(dayCount) {
            var result = [];
            for (var i = 0, len = data0.values.length; i < len; i++) {
                if (i < dayCount) {
                    result.push('-');
                    continue;
                }
                var sum = 0;
                for (var j = 0; j < dayCount; j++) {
                    sum += data0.values[i - j][1];
                }
                result.push(sum / dayCount);
            }
            return result;
        };
                    
        myChart.setOption({
            title: {
            text: 'BTC币',
            left: 0.,
            textStyle:{
                    color:axisFontColor,
                }                             
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross'
                }
            },
            legend: {
                data: ['日K', 'MA5', 'MA10', 'MA20', 'MA30'],
                textStyle:{
                        color:axisFontColor,
                    }
            },
            grid: {
                left: '10%',
                right: '10%',
                bottom: '15%'
            },
            xAxis: {
                type: 'category',
                data: data0.categoryData,
                scale: true,
                boundaryGap: false,
                axisLine: {onZero: false},
                splitLine: {show: false},
                splitNumber: 20,
                min: 'dataMin',
                max: 'dataMax',
                axisLabel:{
                    show:true,
                    textStyle:{
                        color:axisFontColor,
                    }
                },
            },
            yAxis: {
                axisLabel:{
                    show:true,
                    textStyle:{
                        color:axisFontColor,
                    }
                },
                splitLine: {show: false},
                scale: true,
                splitArea: {
                    show: true,
                    areaStyle:{
                        color:[
                            'rgba(10,9,9,0)',
                            'rgba(10,9,9,0)'
                        ],
                    },
                }
            },
            dataZoom: [
                {
                    type: 'inside',
                    start: 95,
                    end: 100
                },
                {
                    show: true,
                    type: 'slider',
                    top: '90%',
                    start: 95,
                    end: 100
                }
            ],
            series: [
                {
                    name: '日K',
                    type: 'candlestick',
                    data: data0.values,
                    itemStyle: {
                        color: upColor,
                        color0: downColor,
                        borderColor: upBorderColor,
                        borderColor0: downBorderColor
                    },
                    markPoint: {
                        label: {
                            normal: {
                                formatter: function (param) {
                                    return param != null ? Math.round(param.value) : '';
                                }
                            }
                        },
                        data: [
                            {
                                name: 'XX标点',
                                coord: ['2013/5/31', 2300],
                                value: 2300,
                                itemStyle: {
                                    color: 'rgb(41,60,85)'
                                }
                            },
                                        {
                                            name: 'highest value',
                                            type: 'max',
                                            valueDim: 'highest'
                                        },
                                        {
                                            name: 'lowest value',
                                            type: 'min',
                                            valueDim: 'lowest'
                                        },
                                        {
                                            name: 'average value on close',
                                            type: 'average',
                                            valueDim: 'close'
                                        }
                                    ],
                                    tooltip: {
                                        formatter: function (param) {
                                            return param.name + '<br>' + (param.data.coord || '');
                                        }
                                    }
                                },
                                markLine: {
                                    symbol: ['none', 'none'],
                                    data: [
                                        [
                                            {
                                                name: 'from lowest to highest',
                                                type: 'min',
                                                valueDim: 'lowest',
                                                symbol: 'circle',
                                                symbolSize: 5,
                                                label: {
                                                    show: false
                                                },
                                                emphasis: {
                                                    label: {
                                                        show: false
                                                    }
                                                }
                                            },
                                            {
                                                type: 'max',
                                                valueDim: 'highest',
                                                symbol: 'circle',
                                                symbolSize: 5,
                                                label: {
                                                    show: false
                                                },
                                                emphasis: {
                                                    label: {
                                                        show: false
                                                    }
                                                }
                                            }
                                        ],
                                        {
                                            name: 'min line on close',
                                            type: 'min',
                                            valueDim: 'close'
                                        },
                                        {
                                            name: 'max line on close',
                                            type: 'max',
                                            valueDim: 'close'
                                        }
                                    ]
                                }
                            },
                            {
                                name: 'MA5',
                                type: 'line',
                                data: calculateMA(5),
                                smooth: true,
                                lineStyle: {
                                    opacity: 0.5
                                }
                            },
                            {
                                name: 'MA10',
                                type: 'line',
                                data: calculateMA(10),
                                smooth: true,
                                lineStyle: {
                                    opacity: 0.5
                                }
                            },
                            {
                                name: 'MA20',
                                type: 'line',
                                data: calculateMA(20),
                                smooth: true,
                                lineStyle: {
                                    opacity: 0.5
                                }
                            },
                            {
                                name: 'MA30',
                                type: 'line',
                                data: calculateMA(30),
                                smooth: true,
                                lineStyle: {
                                    opacity: 0.5,
                                    
                                }
                            },
    
                        ]
        });
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    });
    $.post('/rank_right',function(data){
        // 右侧排行 主流币
        $('#tr_main_coin_1').html('<td><span>1</span></td><td>'+data['1']['0']['0']+'</td><td>'+data['1']['0']['1']+'<br></td><td>'+data['1']['0']['2']+'<br></td>');
        $('#tr_main_coin_2').html('<td><span>2</span></td><td>'+data['1']['1']['0']+'</td><td>'+data['1']['1']['1']+'<br></td><td>'+data['1']['1']['2']+'<br></td>');
        $('#tr_main_coin_3').html('<td><span>3</span></td><td>'+data['1']['2']['0']+'</td><td>'+data['1']['2']['1']+'<br></td><td>'+data['1']['2']['2']+'<br></td>');
        $('#tr_main_coin_4').html('<td><span>4</span></td><td>'+data['1']['3']['0']+'</td><td>'+data['1']['3']['1']+'<br></td><td>'+data['1']['3']['2']+'<br></td>');
        $('#tr_main_coin_5').html('<td><span>5</span></td><td>'+data['1']['4']['0']+'</td><td>'+data['1']['4']['1']+'<br></td><td>'+data['1']['4']['2']+'<br></td>');
        // 左侧排行 山寨币
        $('#tr_not_main_coin_1').html('<td><span>1</span></td><td>'+data['2']['0']['0']+'</td><td>'+data['2']['0']['1']+'<br></td><td>'+data['2']['0']['2']+'<br></td>');
        $('#tr_not_main_coin_2').html('<td><span>2</span></td><td>'+data['2']['1']['0']+'</td><td>'+data['2']['1']['1']+'<br></td><td>'+data['2']['1']['2']+'<br></td>');
        $('#tr_not_main_coin_3').html('<td><span>3</span></td><td>'+data['2']['2']['0']+'</td><td>'+data['2']['2']['1']+'<br></td><td>'+data['2']['2']['2']+'<br></td>');
        $('#tr_not_main_coin_4').html('<td><span>4</span></td><td>'+data['2']['3']['0']+'</td><td>'+data['2']['3']['1']+'<br></td><td>'+data['2']['3']['2']+'<br></td>');
        $('#tr_not_main_coin_5').html('<td><span>5</span></td><td>'+data['2']['4']['0']+'</td><td>'+data['2']['4']['1']+'<br></td><td>'+data['2']['4']['2']+'<br></td>');
    });

    $.post('/rose_echart',function(data){
        var myChart = echarts.init(document.getElementById('rose_echart'));
        // alert(data['0']);
        // var data= $.parseJSON(data);    //将传递过来的json字符串转化为对象
        //alert(data);
        //  console.log(data);
        var servicedata=[];
        for(var i=0;i<data['0'].length;i++){
            var obj=new Object();
            obj.name=data['0'][i]; 
            obj.value=data['1'][i];
            servicedata[i]=obj;
            
        }
        console.log(servicedata);
        option = {
                    tooltip : {
                        trigger: 'item',
                        formatter: "{b} : {c} ({d}%)"
                    },
                    legend: {
                        right:0,
                        top:30,
                        height:160,
                        itemWidth:10,
                        itemHeight:10,
                        itemGap:10,
                        textStyle:{
                            color: 'rgba(255,255,255,.6)',
                            fontSize:12
                        },
                        orient:'vertical',
                        data: data['0']
                    },
                   calculable : true,
                    series : [
                        {
                            name:' ',
							color: ['#62c98d', '#2f89cf', '#4cb9cf', '#205acf', '#c9c862', '#c98b62', '#c962b9', '#7562c9','#c96262','#c25775','#00b7be'],	
                            type:'pie',
                            radius : [30, 70],
                            center : ['35%', '50%'],
                            roseType : 'radius',
                            label: {
                                normal: {
                                    show: true
                                },
                                emphasis: {
                                    show: true
                                }
                            },

                            lableLine: {
                                normal: {
                                    show: true
                                },
                                emphasis: {
                                    show: true
                                }
                            },

                            data:servicedata,
                        },
                    ]
                };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
            });

    });
    

    // 右上方三个圆圈的两个圆圈
    $.post('/k_line_echart',function(data){

        // var myChart1 = echarts.init(document.getElementById('zb1'));
        function zb2(data) {
            // 基于准备好的dom，初始化echarts实例
            var myChart1 = echarts.init(document.getElementById('zb1'));
            var myChart2 = echarts.init(document.getElementById('zb2'));
            datafortwo = []
            for(val in data){
                // alert(data[val]);
                datafortwo.push(data[val]);
            }
            var down_or_rise =datafortwo[1];
            var color_for_second = '#FF0000'
            if(down_or_rise>0){
                down_or_rise = '+'+down_or_rise;
            }
            else{
                down_or_rise = ''+down_or_rise;
                color_for_second = '#00FF00'
            } 
            option1 = {
                series: [{	
                    type: 'pie',
                    radius: ['60%', '70%'],
                    color:'#2ECCFA',
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value:1,
                    name: '',
                    label: {
                        normal: {
                            formatter: datafortwo[0]+'',
                            textStyle: {
                                fontSize: 20,
                                color:'#fff',
                            }
                        }
                    }
                }, {
                    value: 0,
                    name: '',
                    label: {
                        normal: {
                            textStyle: {
                                color: '#aaa',
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: 'rgba(255,255,255,.2)'
                        },
                        emphasis: {
                            color: '#fff'
                        }
                    },
                }]
            }]
        };
            // alert(data1[0]);
          option2 = {
            series: [{	
                type: 'pie',
                radius: ['60%', '70%'],
                color:color_for_second,
            label: {
                normal: {
                    position: 'center'
                }
            },
            data: [{
                value:1,
                name: '',
                label: {
                    normal: {
                        formatter: down_or_rise+'%',
                        textStyle: {
                            fontSize: 20,
                            color:'#fff',
                        }
                    }
                }
            }, {
                value: 0,
                name: '',
                label: {
                    normal: {
                        textStyle: {
                            color: '#aaa',
                            fontSize: 12
                        }
                    }
                },
                itemStyle: {
                    normal: {
                        color: 'rgba(255,255,255,.2)'
                    },
                    emphasis: {
                        color: '#fff'
                    }
                },
            }]
        }]
    };        
        myChart1.setOption(option1)
        myChart2.setOption(option2);
        window.addEventListener("resize",function(){
            myChart1.resize();    
            myChart2.resize();
            });
        }

        for( val in data['2']){
            // alert(data['2'][val]);
            zb2(data['2'][val]);
        };
        

        
    });

    $.post("/predict",function(data){
        var myChart = echarts.init(document.getElementById('predict_echart'));
        x_lable =[]
        y_open =[]
        y_close=[]
        y_high=[]
        y_low=[]
        for(val in data){
            x_lable.push(data[val][0]);
            y_open.push(data[val][1]);
            y_close.push(data[val][2]);
            y_high.push(data[val][3]);
            y_low.push(data[val][4]);
            // console.log(data[val][1]);
            // console.log(data[val][2]);
            // console.log(data[val][3]);
            // console.log(data[val][4]);
        }
        var min_price =999999999;
        for(var i=0;i<y_low.length;i++){
            if(y_low[i]<min_price){
                min_price = y_low[i];
            }
        }
        // alert(min_price);
        option = {
            title: {
                text: 'BTC币',
                textStyle:{
                    color:'rgba(255,255,255,.6)'
                }
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data: ['开盘价格','收盘价格','最高价格','最低价格']
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            // toolbox: {
            //     feature: {
            //         saveAsImage: {}
            //     }
            // },
            xAxis: {
                type: 'category',
                axisLabel:{
                    color:'rgba(255,255,255,.6)'
                },
                data: x_lable
            },
            yAxis: {
                type: 'value',
                min: (min_price*0.999).toFixed(3)
            },
            series: [
                {
                    name: '开盘价格',
                    type: 'line',
                    step: 'start',
                    data: y_open
                },
                {
                    name: '收盘价格',
                    type: 'line',
                    step: 'middle',
                    data: y_close
                },
                {
                    name: '最高价格',
                    type: 'line',
                    step: 'end',
                    data: y_high
                },
                {
                    name: '最低价格',
                    type: 'line',
                    step: 'end',
                    data: y_low
                }
            ]
        };
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
            });

    });
                 
                    
    $(".loading").fadeOut()
})  


$(function () {
    // 设置右侧两个排行榜定时刷新，这里设置为1分钟
    update_right_rank();
    function update_right_rank(){
        setTimeout(update_right_rank,1000*60*1);//1000表示1000ms *60表示一分钟 *1表示一分钟
        $.post('/rank_right',function(data){
            // console.log("nihao");
            // 右侧排行 主流币
            $('#tr_main_coin_1').html('<td><span>1</span></td><td>'+data['1']['0']['0']+'</td><td>'+data['1']['0']['1']+'<br></td><td>'+data['1']['0']['2']+'<br></td>');
            $('#tr_main_coin_2').html('<td><span>2</span></td><td>'+data['1']['1']['0']+'</td><td>'+data['1']['1']['1']+'<br></td><td>'+data['1']['1']['2']+'<br></td>');
            $('#tr_main_coin_3').html('<td><span>3</span></td><td>'+data['1']['2']['0']+'</td><td>'+data['1']['2']['1']+'<br></td><td>'+data['1']['2']['2']+'<br></td>');
            $('#tr_main_coin_4').html('<td><span>4</span></td><td>'+data['1']['3']['0']+'</td><td>'+data['1']['3']['1']+'<br></td><td>'+data['1']['3']['2']+'<br></td>');
            $('#tr_main_coin_5').html('<td><span>5</span></td><td>'+data['1']['4']['0']+'</td><td>'+data['1']['4']['1']+'<br></td><td>'+data['1']['4']['2']+'<br></td>');
            // 左侧排行 山寨币
            $('#tr_not_main_coin_1').html('<td><span>1</span></td><td>'+data['2']['0']['0']+'</td><td>'+data['2']['0']['1']+'<br></td><td>'+data['2']['0']['2']+'<br></td>');
            $('#tr_not_main_coin_2').html('<td><span>2</span></td><td>'+data['2']['1']['0']+'</td><td>'+data['2']['1']['1']+'<br></td><td>'+data['2']['1']['2']+'<br></td>');
            $('#tr_not_main_coin_3').html('<td><span>3</span></td><td>'+data['2']['2']['0']+'</td><td>'+data['2']['2']['1']+'<br></td><td>'+data['2']['2']['2']+'<br></td>');
            $('#tr_not_main_coin_4').html('<td><span>4</span></td><td>'+data['2']['3']['0']+'</td><td>'+data['2']['3']['1']+'<br></td><td>'+data['2']['3']['2']+'<br></td>');
            $('#tr_not_main_coin_5').html('<td><span>5</span></td><td>'+data['2']['4']['0']+'</td><td>'+data['2']['4']['1']+'<br></td><td>'+data['2']['4']['2']+'<br></td>');
        });
    }
    // echarts_1();
	// echarts_2();
	// echarts_3();
	// echarts_4();
	// echarts_5();
	// zb1();
	// zb2();
	zb3(); //沿用模板 设置币种
    function echarts_1() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('rose_echart'));
        option = {
                    tooltip : {
                        trigger: 'item',
                        formatter: "{b} : {c} ({d}%)"
                    },
                    legend: {
                        right:0,
                        top:30,
                        height:160,
                        itemWidth:10,
                        itemHeight:10,
                        itemGap:10,
                        textStyle:{
                            color: 'rgba(255,255,255,.6)',
                            fontSize:12
                        },
                        orient:'vertical',
                        data:['图例1','图例2','图例3','图例4','图例5']
                    },
                   calculable : true,
                    series : [
                        {
                            name:' ',
							color: ['#62c98d', '#2f89cf', '#4cb9cf', '#53b666', '#62c98d', '#205acf', '#c9c862', '#c98b62', '#c962b9', '#7562c9','#c96262','#c25775','#00b7be'],	
                            type:'pie',
                            radius : [30, 70],
                            center : ['35%', '50%'],
                            roseType : 'radius',
                            label: {
                                normal: {
                                    show: true
                                },
                                emphasis: {
                                    show: true
                                }
                            },

                            lableLine: {
                                normal: {
                                    show: true
                                },
                                emphasis: {
                                    show: true
                                }
                            },

                            data:[
                                {value:10, name:'图例1'},
                                {value:5, name:'图例2'},
                                {value:15, name:'图例3'},
                                {value:25, name:'图例4'},
                                {value:20, name:'图例5'},
                      
                            ]
                        },
                    ]
                };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
function echarts_2() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart2'));

        option = {
            tooltip: {
                trigger: 'item',
               formatter: "{b} : {c} ({d}%)"
            },
            legend: {
			
				top:'15%',
                data: ['图例1', '图例2', '图例3', '图例4', '图例5'],
                icon: 'circle',
                textStyle: {
                    color: 'rgba(255,255,255,.6)',
                }
            },
            calculable: true,
            series: [{
                name: '',
				color: ['#62c98d', '#2f89cf', '#4cb9cf', '#53b666', '#62c98d', '#205acf', '#c9c862', '#c98b62', '#c962b9','#c96262'],	
                type: 'pie',
                //起始角度，支持范围[0, 360]
                startAngle: 0,
                //饼图的半径，数组的第一项是内半径，第二项是外半径
                radius: [51, 100],
                //支持设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
                center: ['50%', '45%'],
				
                //是否展示成南丁格尔图，通过半径区分数据大小。可选择两种模式：
                // 'radius' 面积展现数据的百分比，半径展现数据的大小。
                //  'area' 所有扇区面积相同，仅通过半径展现数据大小
                roseType: 'area',
                //是否启用防止标签重叠策略，默认开启，圆环图这个例子中需要强制所有标签放在中心位置，可以将该值设为 false。
                avoidLabelOverlap: false,
                label: {
                    normal: {
                        show: true,
                      //  formatter: '{c}辆'
                    },
                    emphasis: {
                        show: true
                    }
                },
                labelLine: {
                    normal: {
                        show: true,
                        length2: 1,
                    },
                    emphasis: {
                        show: true
                    }
                },
                data: [
                    {value: 1,name: '图例1',},
                    {value: 4,name: '图例2',},
                    {value: 5,name: '图例3',},
                    {value: 6,name: '图例4',},
                    {value: 9,name: '图例5',},
         
                   

                    {value: 0, name: "",label: {show: false},labelLine: {show: false}},
                    {value: 0, name: "",label: {show: false},labelLine: {show: false}},
                    {value: 0, name: "",label: {show: false},labelLine: {show: false}},
                    {value: 0, name: "",label: {show: false},labelLine: {show: false}},
                    {value: 0, name: "",label: {show: false},labelLine: {show: false}},

                   
                ]
            }]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
function echarts_3() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart3'));

        option = {
	tooltip: {
		trigger: 'axis',
		axisPointer: {
			lineStyle: {
				color: '#57617B'
			}
		}
	},
	legend: {
	
		//icon: 'vertical',
			data: ['销售额', '利润'],
        //align: 'center',
       // right: '35%',
		top:'0',
        textStyle: {
            color: "#fff"
        },
       // itemWidth: 15,
       // itemHeight: 15,
        itemGap: 20,
	},
	grid: {
		left: '0',
		right: '20',
		top:'10',
		bottom: '20',
		containLabel: true
	},
	xAxis: [{
		type: 'category',
		boundaryGap: false,
		axisLabel: {
			show: true,
			textStyle: {
                           color: 'rgba(255,255,255,.6)'
                        }
		},
		axisLine: {
			lineStyle: {
				color: 'rgba(255,255,255,.1)'
			}
		},
		data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
	}, {
		

		
		
	}],
	yAxis: [{
		axisLabel: {
			show: true,
			textStyle: {
                           color: 'rgba(255,255,255,.6)'
                        }
		},
		axisLine: {
			lineStyle: {
				color: 'rgba(255,255,255,.1)'
			}
		},
		splitLine: {
			lineStyle: {
				color: 'rgba(255,255,255,.1)'
			}
		}
	}],
	series: [{
		name: '销售额',
		type: 'line',
		smooth: true,
		symbol: 'circle',
		symbolSize: 5,
		showSymbol: false,
		lineStyle: {
			normal: {
				width: 2
			}
		},
		areaStyle: {
			normal: {
				color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
					offset: 0,
					color: 'rgba(24, 163, 64, 0.3)'
				}, {
					offset: 0.8,
					color: 'rgba(24, 163, 64, 0)'
				}], false),
				shadowColor: 'rgba(0, 0, 0, 0.1)',
				shadowBlur: 10
			}
		},
		itemStyle: {
			normal: {
				color: '#cdba00',
				borderColor: 'rgba(137,189,2,0.27)',
				borderWidth: 12
			}
		},
		data: [220, 182, 191, 134, 150, 120, 110, 125, 145, 122, 165, 122]
	}, {
		name: '利润',
		type: 'line',
		smooth: true,
		symbol: 'circle',
		symbolSize: 5,
		showSymbol: false,
		lineStyle: {
			normal: {
				width: 2
			}
		},
		areaStyle: {
			normal: {
				color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
					offset: 0,
					color: 'rgba(39, 122,206, 0.3)'
				}, {
					offset: 0.8,
					color: 'rgba(39, 122,206, 0)'
				}], false),
				shadowColor: 'rgba(0, 0, 0, 0.1)',
				shadowBlur: 10
			}
		},
		itemStyle: {
			normal: {
				color: '#277ace',
				borderColor: 'rgba(0,136,212,0.2)',
				borderWidth: 12
			}
		},
		data: [120, 110, 125, 145, 122, 165, 122, 220, 182, 191, 134, 150]
	}]
};

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
function echarts_4() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart4'));
option = {
   	tooltip: {
		trigger: 'axis',
		axisPointer: {
			lineStyle: {
				color: '#57617B'
			}
		}
	},
    "legend": {
		
      "data": [
        {"name": "图例1"},
        {"name": "图例2"},
        {"name": "完成率"}
      ],
      "top": "0%",
      "textStyle": {
       "color": "rgba(255,255,255,0.9)"//图例文字
      }
    },
	
    "xAxis": [
      {
        "type": "category",
		
        data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
		 axisLine: { lineStyle: {color: "rgba(255,255,255,.1)"}},
        axisLabel:  { textStyle: {color: "rgba(255,255,255,.6)", fontSize: '14', },
            },
		
        },
	],
    "yAxis": [
      {
        "type": "value",
        "name": "金额",
        "min": 0,
        "max": 50,
        "interval": 10,
        "axisLabel": {
          "show": true,
         
        },
        axisLine: {lineStyle: {color: 'rgba(255,255,255,.4)'}},//左线色
        
      },
      {
        "type": "value",
        "name": "完成率",
        "show": true,
        "axisLabel": {
          "show": true,
        
        },
		  axisLine: {lineStyle: {color: 'rgba(255,255,255,.4)'}},//右线色
		   splitLine: {show:true,lineStyle: {color:"#001e94"}},//x轴线
      },
    ],
    "grid": {
      "top": "10%",
		"right":"30",
		"bottom":"30",
		"left":"30",
    },
    "series": [
      {
        "name": "图例1",
		  
        "type": "bar",
        "data": [4,6,36,6,8,6,4,6,30,6,8,12],
        "barWidth": "auto",
        "itemStyle": {
          "normal": {
            "color": {
              "type": "linear",
              "x": 0,
              "y": 0,
              "x2": 0,
              "y2": 1,
              "colorStops": [
                {
                  "offset": 0,
                  "color": "#609db8"
                },
                
                {
                  "offset": 1,
                  "color": "#609db8"
                }
              ],
              "globalCoord": false
            }
          }
        }
      },
      {
        "name": "图例2",
        "type": "bar",
        "data": [
          4,2,34,6,8,6,4,2,32,6,8,18
        ],
        "barWidth": "auto",
		
        "itemStyle": {
          "normal": {
            "color": {
              "type": "linear",
              "x": 0,
              "y": 0,
              "x2": 0,
              "y2": 1,
              "colorStops": [
                {
                  "offset": 0,
                  "color": "#66b8a7"
                },
                {
                  "offset": 1,
                  "color": "#66b8a7"
                }
              ],
              "globalCoord": false
            }
          }
        },
        "barGap": "0"
      },
      {
        "name": "完成率",
        "type": "line",
        "yAxisIndex": 1,
		
        "data": [100,50,80,30,90,40, 70,33,100,40,80,20],
		  lineStyle: {
			normal: {
				width: 2
			},
		},
        "itemStyle": {
          "normal": {
            "color": "#cdba00",
			 
          }
        },
        "smooth": true
      }
    ]
};
       

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
	
function echarts_5() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart5'));
// 颜色
var lightBlue = {
	type: 'linear',
	x: 0,
	y: 0,
	x2: 0,
	y2: 1,
	colorStops: [{
		offset: 0,
		color: 'rgba(41, 121, 255, 1)'
	}, {
		offset: 1,
		color: 'rgba(0, 192, 255, 1)'
	}],
	globalCoord: false
}

var option = {
	tooltip: {
		show: false
	},
	grid: {
		top: '0%',
		left: '65',
		right: '14%',
		bottom: '0%',
	},
	xAxis: {
		min: 0,
		max: 100,
		splitLine: {
			show: false
		},
		axisTick: {
			show: false
		},
		axisLine: {
			show: false
		},
		axisLabel: {
			show: false
		}
	},
	yAxis: {
		data: ['字段名称', '字段名称', '字段名称','字段名称','字段名称','字段名称','字段名称','字段名称','字段名称','字段名称','字段名称'],
		//offset: 15,
		axisTick: {
			show: false
		},
		axisLine: {
			show: false
		},
		axisLabel: {
			color: 'rgba(255,255,255,.6)',
			fontSize: 14
		}
	},
	series: [{
		type: 'bar',
		label: {
			show: true,
			zlevel: 10000,
			position: 'right',
			padding: 10,
			color: '#49bcf7',
			fontSize: 14,
			formatter: '{c}%'
			
		},
		itemStyle: {
			color:'#49bcf7'
		},
		barWidth: '15',
		data: [49, 80, 67, 99, 12, 19, 39, 84, 28, 47, 57, 100],
		z: 10
	}, {
		type: 'bar',
		barGap: '-100%',
		itemStyle: {
			color:'#fff',
			opacity: 0.1
		},
		barWidth: '15',
		data: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
		z: 5
	}],
};
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
	
	
function zb1() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb1'));
        var symbol ="BTC"
	    var v1=298//男消费
		var v2=523//女消费
		var v3=v1+v2//总消费 
option = {	
    series: [{
		
        type: 'pie',
        radius: ['60%', '70%'],
        color:'#49bcf7',
        label: {
            normal: {
                position: 'center'
            }
        },
        data: [{
            value: 'BTC',
            label: {
                normal: {
                    formatter: "BTC",
                    textStyle: {
                        fontSize: 20,
						color:'#fff',
                    }
                }
            }
        }, {
            value: v1,

            label: {
                normal: {
                 formatter : function (params){
                return '占比'+Math.round( v2/v3*100)+ '%'
            },
                    textStyle: {
                        color: '#aaa',
                        fontSize: 12
                    }
                }
            },
            itemStyle: {
                normal: {
                    color: 'rgba(255,255,255,.2)'
                },
                emphasis: {
                    color: '#fff'
                }
            },
        }]
    }]
};
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
function zb2(data) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb2'));
        
        alert(data[0]);
      option = {
    series: [{	
        type: 'pie',
       radius: ['60%', '70%'],
        color:'#cdba00',
        label: {
            normal: {
                position: 'center'
            }
        },
        data: [{
            value:10,
            name: '',
            label: {
                normal: {
                    formatter: data[0],
                    textStyle: {
                        fontSize: 20,
						color:'#fff',
                    }
                }
            }
        }, {

            value: 0,
            name: '',
            label: {
                normal: {
                    textStyle: {
                        color: '#aaa',
                        fontSize: 12
                    }
                }
            },
            itemStyle: {
                normal: {
                    color: 'rgba(255,255,255,.2)'
                },
                emphasis: {
                    color: '#fff'
                }
            },
        }]
    }]
};
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
function zb3() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb3'));
		// var v1=298//男消费
		// var v2=523//女消费
		// var v3=v1+v2//总消费 
option = {	
    series: [{
		
        type: 'pie',
       radius: ['60%', '70%'],
        color:'#62c98d',
        label: {
            normal: {
                position: 'center'
            }
        },
        data: [{
            value: 1,
            name: '',
            label: {
                normal: {
                    formatter: 100 +'',
                    textStyle: {
                        fontSize: 20,
						color:'#fff',
                    }
                }
            }
        }, {
            value: 0,
            name: '',
            label: {
                normal: {
            //      formatter : function (params){
            //     return '占比'+Math.round( v2/v3*100)+ '%'
            // },
                    textStyle: {
                        color: '#aaa',
                        fontSize: 12
                    }
                }
            },
            itemStyle: {
                normal: {
                    color: 'rgba(255,255,255,.2)'
                },
                emphasis: {
                    color: '#fff'
                }
            },
        }]
    }]
};
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }
})



		
		
		


		









