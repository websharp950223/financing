robo.define('web_gantt_native.ToolTip', function (require) {
"use strict";


var core = require('web.core');
var Widget = require('web.Widget');
var time = require('web.time');
var _t = core._t;



var GanttToolTip = Widget.extend({
    template: "GanttToolTip",

   /// this.chart.tooltip.show(this.resizerOffsetX, this);

    init: function(parent, ganttbar) {

        this._super(parent);
        this.record = ganttbar;

    },

    start: function() {


        var self = this;

        this.$el.append('<div class="task-gantt-line-tip-names"></div>');

        var record = self.record[0];

        if (record) {

            var record_data = record.record;

            var name = record_data['value_name'];

            // var task_start = record_data['task_start'].toUTCString()
            //
            // var ttt = record_data.task_start;

            // var formatDate = "DD.MM.YYYY HH:mm:ss"; // the string that represents desired format.
            var l10n = _t.database.parameters;

            var formatDate = time.strftime_to_moment_format( l10n.date_format + ' ' + l10n.time_format);


            // var task_start = time.auto_date_to_str(record_data.task_start, 'datetime');


            var task_start = moment(record_data["task_start"]).format(formatDate);
            var task_stop = moment(record_data["task_stop"]).format(formatDate);

            var date_deadline = false;
            if (record_data["date_deadline"]) {

                date_deadline = moment(record_data["date_deadline"]).format(formatDate);
            }


            // var task_stop = record_data['task_stop'];
            // task_stop = time.auto_date_to_str(task_stop, 'datetime');

            // var date_deadline = record_data['date_deadline'];
            // date_deadline = time.auto_date_to_str(date_deadline, 'datetime');

            var progress = '';
            var progress_name = 'Progresas';
            if (record_data['progress']){
                progress = record_data['progress'];

                var progress_field = self.__parentedParent.model_fields_dict['progress'];
                //ROBO: lets hide due to translation f'cup
                // if (progress_field){
                //     progress_name = self.__parentedParent.fields[progress_field].string;
                // }
                self.__parentedParent.fields[''];
                // progress_name
                //self.model_fields_dict = getFields["model_fields_dict"];

            }

            var date_done = false;
            if (record_data["date_done"]) {

                date_done = moment(record_data["date_done"]).format(formatDate);

            }

            var duration = false;
            if (record_data["duration"]) {
                var total = parseInt(record_data["duration"], 10);

                if (record_data['duration_scale']) {
                    duration = humanizeDuration(total*1000,{ units: record_data['duration_scale'].split(","), language:'lt'});
                }
                else{
                    duration = humanizeDuration(total*1000, {language:'lt'});
                }

            }

            var plan_duration = false;
            if (record_data["plan_duration"]) {
                var plan_total = parseInt(record_data["plan_duration"], 10);

                if (record_data['duration_scale']) {
                    plan_duration = humanizeDuration(plan_total*1000,{ units: record_data['duration_scale'].split(","), language: 'lt'});
                }
                else{
                    plan_duration = humanizeDuration(plan_total*1000, {language:'lt'});
                }

            }





            var constrain_type = false;
            if (record_data['constrain_type']){


                var type = [];

                type["asap"] = _t('Kaip įmanoma greičiau/vėliau');
                type["fnet"] = _t('Pradėti neanksčiau kaip');
                type["fnlt"] = _t('Pabaigti nevėliau kaip');
                type["mso"] = _t('Privalo prasidėti');
                type["mfo"] = _t('Privalo baigtis');
                type["snet"] = _t('Pradėti neanksčiau kaip');
                type["snlt"] = _t('Pradėti nevėliau kaip');

                constrain_type = type[record_data['constrain_type']];


            }

            var constrain_date = "-";
            if (record_data["constrain_date"]) {

                constrain_date = moment(record_data["constrain_date"]).format(formatDate);

            }





            $('<div class="task-gantt-line-tip-name">Pavadinimas:</div>').appendTo(this.$el.children(".task-gantt-line-tip-names"));
            $('<div class="task-gantt-line-tip-name">Pradžia:</div>').appendTo(this.$el.children(".task-gantt-line-tip-names"));
            $('<div class="task-gantt-line-tip-name">Pabaiga:</div>').appendTo(this.$el.children(".task-gantt-line-tip-names"));
            $('<div class="task-gantt-line-tip-name">Terminas:</div>').appendTo(this.$el.children(".task-gantt-line-tip-names"));
            $('<div class="task-gantt-line-tip-name">'+progress_name+'</div>').appendTo(this.$el.children(".task-gantt-line-tip-names"));

            if (date_done) {
                 $('<div class="task-gantt-line-tip-name">Įvykdymo data:</div>').appendTo(this.$el.children(".task-gantt-line-tip-names"));
            }

            if (plan_duration) {
                 $('<div class="task-gantt-line-tip-name">Planuojama trukmė:</div>').appendTo(this.$el.children(".task-gantt-line-tip-names"));
            }

            if (duration) {
                 $('<div class="task-gantt-line-tip-name">Trukmė:</div>').appendTo(this.$el.children(".task-gantt-line-tip-names"));
            }

            if (constrain_type) {
                 $('<div class="task-gantt-line-tip-name">Apribojimai:</div>').appendTo(this.$el.children(".task-gantt-line-tip-names"));
            }

            this.$el.append('<div class="task-gantt-line-tip-values"></div>');




            $('<div class="task-gantt-line-tip-value">' + (name || '-') + '</div>').appendTo(this.$el.children(".task-gantt-line-tip-values"));
            $('<div class="task-gantt-line-tip-value">' + (task_start || '-')  + '</div>').appendTo(this.$el.children(".task-gantt-line-tip-values"));
            $('<div class="task-gantt-line-tip-value">' + (task_stop || '-') + '</div>').appendTo(this.$el.children(".task-gantt-line-tip-values"));
            $('<div class="task-gantt-line-tip-value">' + (date_deadline || '-') + '</div>').appendTo(this.$el.children(".task-gantt-line-tip-values"));
            $('<div class="task-gantt-line-tip-value">' + (progress || '-') + '%</div>').appendTo(this.$el.children(".task-gantt-line-tip-values"));

            if (date_done) {
                $('<div class="task-gantt-line-tip-value">' + (date_done || '') + '</div>').appendTo(this.$el.children(".task-gantt-line-tip-values"));
            }
            if (plan_duration) {
                $('<div class="task-gantt-line-tip-value">' + (plan_duration || '')+ '</div>').appendTo(this.$el.children(".task-gantt-line-tip-values"));
            }

            if (duration) {
                $('<div class="task-gantt-line-tip-value">' + (duration || '')+ '</div>').appendTo(this.$el.children(".task-gantt-line-tip-values"));
            }

            if (constrain_type) {
                $('<div class="task-gantt-line-tip-value">' + (constrain_type || '') + ': ' + (constrain_date || '-')+ '</div>').appendTo(this.$el.children(".task-gantt-line-tip-values"));
            }


        }

        if (self.record.offset()) {

            var o_left = self.record.offset().left;
            var o_top = self.record.offset().top;

            var o_right = $(window).width() - (self.record.offset().left + self.record.outerWidth());


            var tip_lenght = this.$el.children(".task-gantt-line-tip-names").children().length;
            var top_new = o_top - (15*tip_lenght); // if added tip plus 15 every tip

            //ROBO: < 325 ??
            // if (o_top < 325){
            //     top_new = o_top + 20;
            // }
            var bound_top = $('.task-gantt-timeline').offset().top;
            if (top_new < bound_top){
                top_new =  o_top + 20;
            }

            if (o_right < 200){
                o_left = o_left - 200;
            }


            this.$el.offset({top: top_new , left: o_left});
        }


    },


    renderElement: function () {
        this._super();
        this.$el.data('record', this);

    },



});

return GanttToolTip;

});