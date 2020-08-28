// Example 1

function square(num){
    return num * num;
}

var f = square(5)

console.log(square)
console.log(f)

// Example 2

function square(num){
    return num * num;
}

function cube(num){
    return num * num * num;
}

function my_map(func, arg_list){
    result = [];
    for(var i = 0; i < arg_list.length; i++ ){
        result.push(func(arg_list[i]))
    }
    return result;
}

var squares = my_map(cube, [1, 2, 3, 4, 5])
console.log(squares)


// Example 3

function logger(msg){
    function log_message(){
        console.log('Log: ' + msg)
    }
    return log_message
}

log_hi = logger('Hello')
log_hi()


// Example 4

function html_tag(tag){
    function html_text(text){
        console.log('<' + tag + '>' + text + '</' + tag + '>');
    }
    return html_text;
}

var tag_h1 = html_tag('h1')
tag_h1('This is a h1 text')

var tag_p = html_tag('p')
tag_p('This is a paragraph')