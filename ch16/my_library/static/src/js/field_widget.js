odoo.define('my_field_widget', function (require) {
    "use strict";

    const { Component } = owl;
    const AbstractField = require('web.AbstractFieldOwl');   //創建字段的基礎元素
    const fieldRegistry = require('web.field_registry_owl');  //字段組件

    // 6新增組件，載入樣板，增加方法。
    class ColorPill extends Component {
        static template = 'OWLColorPill';
        pillClicked() {
            this.trigger('color-updated', {val: this.props.pill_no});
        }
    }

    // 7導入新增的組件
    class FieldColor extends AbstractField {
        static supportedFieldTypes = ['integer'];
        static template = 'OWLFieldColorPills';
        static components = { ColorPill };

        constructor(...args) {
            super(...args);
            this.totalColors = Array.from({length: 10}, (_, i) => (i + 1).toString());
        }
        //8RPC紀錄
        async willStart() {
            this.colorGroupData = {};
            var colorData = await this.rpc({
                model: this.model, method: 'read_group',
                domain: [], fields: ['color'],
                groupBy: ['color'],
            });
            colorData.forEach(res => {
                this.colorGroupData[res.color] = res.color_count;
            });
        }
        //儲存到資料庫
        colorUpdated(ev) {
            this._setValue(ev.detail.val);
        }
    }

    //9註冊組建，使widget可以使用
    fieldRegistry.add('int_color', FieldColor);

    return {
        FieldColor: FieldColor,
    };
});
