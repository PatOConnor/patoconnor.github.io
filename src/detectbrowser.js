var detectPortrait = () => {
    // checks if user is in portrait mode by comparing screen height and width
    let ratio = screen.availWidth / screen.availHeight
    console.log(ratio)
    return true ? ratio < 0.7: false;

}

var assignLayout = () => {
    let portraitMode = detectPortrait()
    let cssLink = document.createElement('link')
    cssLink.setAttribute('rel', 'stylesheet')
    if (portraitMode) {
        cssLink.setAttribute('href', './static/styles/mobile-layout.css')
    } else {
        cssLink.setAttribute('href', './static/styles/desktop-layout.css')
    }
    let head = document.getElementsByTagName('head')[0]
    head.appendChild(cssLink)
}