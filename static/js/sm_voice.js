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
                                    per_page: response.page,
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
                debugger;
            }
        )
    },
    onConfirmSurvey: function(e){
        $.post("/collectors", {survey_id: this.state.selected_survey}, function(response, status){
           alert(this.state.selected_survey);
        });
    },
    render: function(){
        var surveys = this.state.surveys;
        return (
          <div><SurveyListRender surveys={surveys} onSurveySelect={this.onSurveySelect} /></div>
        );
    }

});

lol = ReactDOM.render(
    <SelectSurveyComponent/>,
    document.getElementById('smcontent')
);