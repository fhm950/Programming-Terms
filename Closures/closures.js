// Similer as python example 1
function html_tag(tag){
    function html_text(msg){
        console.log('<' + tag + '>' + msg + '</' + tag + '>')
    }
    return html_text
}

tag_h1 = html_tag('h1')
tag_h1('this is a h1 text')

tag_p = html_tag('p')
tag_p('this is a paragraph')