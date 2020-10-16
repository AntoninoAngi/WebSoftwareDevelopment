

function keywordusage(text, keywords){
      var keylength = keywords.length;
      var array = [];
      for (var i = 0; i < keylength; i++){
          var string = keywords[i];
          array.push(text.includes(string));
      }
      return array;
}

function frequencies(text, wordlist) {
    var words = text.split(/\s/);
    var freqMap = {};
    words.forEach(function(w) {
      if (wordlist && wordlist.indexOf(w) > -1) {
        if (!freqMap[w]) {
          freqMap[w] = 0;
        }
        freqMap[w] += 1;
      }
    });
    return freqMap;
}

function rotate(array, steps = 1){
    steps = Math.floor(steps / array.length) * array.length - steps;
    return array.slice(steps).concat(array.slice(0, steps));
}