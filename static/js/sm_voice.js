$( "#tapitest" ).click(function() {
  $.post("/tapitest", {to: $("#to").val()}, function() {
        alert( "Successfully talked to backend. Wait for your phone to ring." );
    })
    .fail(function(xhr, status, error) {
        alert( "Phone number or API error \n" + error);
    });
});


function check_survey(sid) {
  $.post("/select_survey", {survey_id: sid}, function(response) {
        alert( "Successfully talked to backend: " + response );
    })
    .fail(function(xhr, status, error) {
        alert( "Incompatible survey or survey id error or API error \n" + error);
    });
}


var SurveyListRender = React.createClass({
    render: function() {
        var self = this;
          return (
                <div className="list-group">
                    {this.props.surveys.map(function(survey, i){
                    return<a href="#" key={i} className="list-group-item" value={survey.id} onClick={() =>self.props.onSurveySelect(survey.id)} >{survey.title}</a>
                    })}
                </div>
          )
    }
});

var SelectSurveyComponent = React.createClass({
    getInitialState: function(){
        return {
            surveys: [],
            selected_survey: null,
            selected_collector: null,
            page_num: 1,
            per_page: 10,
            prev: false,
            next: false,
            total: null,
        };
    },
    componentDidMount: function(){
        this.request = $.get("/smapitest", {page: this.page, per_page: this.per_page}, function(response, status){
                                this.setState({
                                    surveys: response.data,
                                    total: response.total,
                                    page: response.page,
                                    per_page: response.per_page,
                                    prev: (response.page > 1)? true : false,
                                    next: (response.page * response.per_page <= response.total)? true : false,
                                });
                            }.bind(this));
    },
    componentWillUnmount: function(){
        this.request.abort();
    },
    onSurveySelect: function(surveyid) {
        this.setState({
            selected_survey: surveyid
        }
        ,function (){
            alert("set a survey! " + this.state.selected_survey);
            // check_survey(this.state.selected_survey)
        }
        )
    },
    onConfirmSurvey: function(e){
        $.post("/collectors", {survey_id: this.state.selected_survey}, function(response, status){
           alert(this.state.selected_survey);
        });
    },
    onNextPrev: function(nextprev){
        this.request = $.get("/smapitest", {page: this.state.page + nextprev, per_page: this.state.per_page}, function(response, status){
                            this.setState({
                                    surveys: response.data,
                                    total: response.total,
                                    page: response.page,
                                    per_page: response.per_page,
                                    prev: (response.page > 1)? true : false,
                                    next: (response.page * response.per_page <= response.total)? true : false,
                                });
                            }.bind(this));
    },
    render: function(){
        var surveys = this.state.surveys;
        return (
          <div>
              <SurveyListRender surveys={surveys} onSurveySelect={this.onSurveySelect} />
              <button disabled={!this.state.prev} onClick={() => this.onNextPrev(-1)} className="button">Prev</button><button disabled={!this.state.next} onClick={() => this.onNextPrev(1)} className="button">Next</button>
          </div>
        );
    }

});

ReactDOM.render(
    <SelectSurveyComponent/>,
    document.getElementById('smcontent')
);