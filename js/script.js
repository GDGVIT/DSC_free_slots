console.log('loaded');

$(document).ready(function () {
    console.log('ready');

});
document.body.addEventListener('click', function (e) {
    e.target.update && e.target.update();
});

if (!window.customElements || !document.head.attachShadow) {
    document.querySelector('html').className += ' oldie'
}

function submitDet() {
    let imageFile = document.getElementById('imageFile');
    let name = $('#name').val().toLowerCase();
    let regNo = $('#regNo').val().toLowerCase();
    if (imageFile.files[0].type === 'image/png') {
        console.log(name, regNo, imageFile.files[0], imageFile.files[0].type);
        let formData = new FormData();
        formData.append('name', name);
        formData.append('regNo', regNo);
        formData.append('timetable', imageFile.files[0]);
        $.ajax({
            url: "http://127.0.0.1:5000/upload",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            type: 'POST',
            success: function (data) {
                console.log(data);
                alert(data);
                window.location.reload();
            }
        })
    }
    else {
        alert('Please upload a PNG file');
    }
}

var tabId = [];
var day = '';

function removetabId(ele) {
    console.log(ele);
    var index = tabId.indexOf(parseInt(ele, 10));
    console.log(index);
    tabId.splice(index, 1);
    console.log(tabId);
    if (!tabId.length) {
        day = '';
    }
}

function pushtabId(ele, dayDet) {
    tabId.push(parseInt(ele, 10));
    console.log(tabId);
    if (tabId.length) {
        day = dayDet
    }
}

$('td').on('click', function () {
    var ele = $(this).attr('tabId');
    if ($(this).hasClass('tdSelected')) {
        console.log(ele);
        removetabId(ele);
    }
    else {
        pushtabId(ele, $(this).parent().attr('id'));
    }
    $(this).toggleClass('tdSelected');
    console.log($(this).attr('tabId'), $(this).parent().attr('id'));
});

function findMembers() {
    var data = {day, tabId};
    console.log(data);
    $.ajax({
        url: 'http://127.0.0.1:5000/findMembers',
        data: JSON.stringify(data),
        cache: false,
        processData: false,
        contentType: 'application/json;charset=UTF-8',
        type: 'POST',
        success: function (data) {
            listMembers(data);
        }

    })
}

function displayTimeTable(data) {
    var t = "<table class=\"centered\">\n" +
        "            <thead>\n" +
        "            <tr>\n" +
        "                <th>Start</th>\n" +
        "                <th>8:00</th>\n" +
        "                <th>9:00</th>\n" +
        "                <th>10:00</th>\n" +
        "                <th>11:00</th>\n" +
        "                <th>12:00</th>\n" +
        "                <th>13:00</th>\n" +
        "                <th>14:00</th>\n" +
        "                <th>15:00</th>\n" +
        "                <th>16:00</th>\n" +
        "                <th>17:00</th>\n" +
        "                <th>18:00</th>\n" +
        "            </tr>\n" +
        "            <tr>\n" +
        "                <th>End</th>\n" +
        "                <th>9:00</th>\n" +
        "                <th>10:00</th>\n" +
        "                <th>11:00</th>\n" +
        "                <th>12:00</th>\n" +
        "                <th>13:00</th>\n" +
        "                <th>14:00</TH>\n" +
        "                <th>15:00</th>\n" +
        "                <th>16:00</th>\n" +
        "                <th>17:00</th>\n" +
        "                <th>18:00</th>\n" +
        "                <th>19:00</th>\n" +
        "            </tr>\n" +
        "            </thead>\n" +
        "            <tbody>\n" +
        "            <tr id=\"monday\">\n" +
        "                <th><b>MONDAY</b></th>\n" +
        "                <td tabId=\"1\">A1</td>\n" +
        "                <td tabId=\"6\">F1</td>\n" +
        "                <td tabId=\"11\">D1</td>\n" +
        "                <td tabId=\"16\">TB1</td>\n" +
        "                <td tabId=\"21\">TG1</td>\n" +
        "                <td rowspan=\"5\"><b>LUNCH</b></td>\n" +
        "                <td tabId=\"31\">A2</td>\n" +
        "                <td tabId=\"36\">F2</td>\n" +
        "                <td tabId=\"41\">D2</td>\n" +
        "                <td tabId=\"46\">TB2</td>\n" +
        "                <td tabId=\"51\">TG2</td>\n" +
        "            </tr>\n" +
        "            <tr id=\"tuesday\">\n" +
        "                <th><b>TUESDAY</b></th>\n" +
        "                <td tabId=\"2\">B1</td>\n" +
        "                <td tabId=\"7\">G1</td>\n" +
        "                <td tabId=\"12\">E1</td>\n" +
        "                <td tabId=\"17\">TC1</td>\n" +
        "                <td tabId=\"22\">TAA1</td>\n" +
        "                <td tabId=\"32\">B2</td>\n" +
        "                <td tabId=\"37\">G2</td>\n" +
        "                <td tabId=\"42\">E2</td>\n" +
        "                <td tabId=\"47\">TC2</td>\n" +
        "                <td tabId=\"52\">TAA2</td>\n" +
        "            </tr>\n" +
        "            <tr id=\"wednesday\">\n" +
        "                <th><b>WEDNESDAY</b></th>\n" +
        "                <td tabId=\"3\">C1</td>\n" +
        "                <td tabId=\"8\">A1</td>\n" +
        "                <td tabId=\"13\">F1</td>\n" +
        "                <td colspan=\"2\" tabId=\"18\">EXTRAMURAL HOUR</td>\n" +
        "                <td tabId=\"33\">C2</td>\n" +
        "                <td tabId=\"38\">A2</td>\n" +
        "                <td tabId=\"43\">F2</td>\n" +
        "                <td tabId=\"48\">TD2</td>\n" +
        "                <td tabId=\"53\">TBB2</td>\n" +
        "            </tr>\n" +
        "            <tr id=\"thursday\">\n" +
        "                <th><b>THURSDAY</b></th>\n" +
        "                <td tabId=\"4\">D1</td>\n" +
        "                <td tabId=\"9\">B1</td>\n" +
        "                <td tabId=\"14\">G1</td>\n" +
        "                <td tabId=\"19\">TE1</td>\n" +
        "                <td tabId=\"24\">TCC1</td>\n" +
        "                <td tabId=\"34\">D2</td>\n" +
        "                <td tabId=\"39\">B2</td>\n" +
        "                <td tabId=\"44\">G2</td>\n" +
        "                <td tabId=\"49\">TE2</td>\n" +
        "                <td tabId=\"54\">TCC2</td>\n" +
        "            </tr>\n" +
        "            <tr id=\"friday\">\n" +
        "                <th><b>FRIDAY</b></th>\n" +
        "                <td tabId=\"5\">E1</td>\n" +
        "                <td tabId=\"10\">C1</td>\n" +
        "                <td tabId=\"15\">TA1</td>\n" +
        "                <td tabId=\"20\">TF1</td>\n" +
        "                <td tabId=\"25\">TD1</td>\n" +
        "                <td tabId=\"35\">E2</td>\n" +
        "                <td tabId=\"40\">C2</td>\n" +
        "                <td tabId=\"45\">TA2</td>\n" +
        "                <td tabId=\"50\">TF2</td>\n" +
        "                <td tabId=\"55\">TDD2</td>\n" +
        "            </tr>\n" +
        "            </tbody>\n" +
        "        </table>";


    $('.searchResult').html(t);
    data["slots"].forEach(details=>{
        $(`td[tabId='${details}']`).addClass('available')
    })
}

function searchMember() {
    var name = $('#memberName').val().toLowerCase();
    var day = $('#days').val();
    var data = {name, day};
    $.ajax({
        url: 'http://127.0.0.1:5000/searchMember',
        data: JSON.stringify(data),
        cache: false,
        processData: false,
        contentType: 'application/json;charset=UTF-8',
        type: 'POST',
        success: function (data) {
            displayTimeTable(data);
        }
    })
}

var nameDetails;

function setColor(name) {
    $('td').removeClass('available');
    console.log(name);
    const index = nameDetails.findIndex((ele) => ele.name.toUpperCase() === name);
    console.log(index);
    let cno = nameDetails[index].timings.container_nos;
    cno.forEach(e => {
        console.log(e);
        $(`td[tabId='${e}']`).addClass('available')
    });
}

function listMembers(data) {
    console.log(data);
    nameDetails = data;
    var t = '<ul class="collapsible">';
    data.map(ele => {
        let timings = '<ul>';
        ele["timings"]["time_slots"].forEach(e => {
            timings += `<li>${e}</li>`;
        });
        timings += '</ul>';
        t += `<li class="names" onclick="setColor(event.target.textContent)">
      <div class="collapsible-header">${ele["name"].toUpperCase()}</div>
      <div class="collapsible-body"><span><h6><b>Free hours: ${ele["free_hrs"]}</b></h6><h6><b>Free Timings</b></h6> ${timings}</span></div>
    </li>`
    });
    t += '</ul>';
    $(".nameList").html(t);
    $(".nameList").css({"display": "block", "align-self": "center"});
    $('.collapsible').collapsible();

}

function reset() {
    $('td').removeClass('available tdSelected');
}

