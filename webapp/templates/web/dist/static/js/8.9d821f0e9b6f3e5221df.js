webpackJsonp([8],{"25KM":function(e,t){},pSIG:function(e,t,s){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o=s("Dd8w"),r=s.n(o),n=s("D4TX"),i=s("gyMJ"),a=s("NYxO"),c={components:{Crumbs:n.a},data:function(){return{form:{name:"",tel:"",remarks:"",address:""},dialogVisible:!1,rules:{name:[{required:!0,message:"请输入客户姓名",trigger:"blur"}],tel:[{required:!0,message:"请输入电话号码",trigger:"blur"}],address:[{required:!0,message:"请输入客户住址",trigger:"blur"}]},goodsList:[],stocks:[],checkedStocks:[],repay:{repayMoney:"",repayTime:""},repayList:[]}},computed:r()({},Object(a.c)(["userInfo"]),{currentAmount:function(){var e=0;return this.goodsList.map(function(t){e+=t.stock_price*t.stock_num}),e},perAmount:function(){this.goodsList.map(function(e){return e.stock_price=+e.stock_price,e.stock_num=+e.stock_num,e.stock_amount=e.stock_price*e.stock_num})}}),methods:r()({},Object(a.b)(["TOSAST_STATE","GET_USERINFO","REMOVE_USERINFO"]),{onSubmitCus:function(){var e=this;this.$refs.rulesform.validate(function(t){if(!t)return!1;var s={token:e.userInfo.token,username:e.userInfo.user,id:e.$route.params.id,form:e.form};Object(i.v)(s).then(function(t){e.TOSAST_STATE({text:t.msg}),2==t.errcode&&(e.REMOVE_USERINFO(),e.$router.push("/login"))})})},onSubmitGoods:function(){var e=this,t={token:this.userInfo.token,username:this.userInfo.user,id:this.$route.params.id,goodsList:this.goodsList};Object(i.u)(t).then(function(t){e.TOSAST_STATE({text:t.msg}),2==t.errcode&&(e.REMOVE_USERINFO(),e.$router.push("/login"))})},judgeRepayMoney:function(){return!!this.repay.repayMoney||(this.TOSAST_STATE({text:"请输入付款金额"}),!1)},judgeRepayTime:function(){return!!this.repay.repayTime||(this.TOSAST_STATE({text:"请选择付款日期"}),!1)},addRepay:function(){var e=this;if(this.judgeRepayMoney()&&this.judgeRepayTime()){var t={token:this.userInfo.token,username:this.userInfo.user,id:this.$route.params.id,amount:this.repay.repayMoney,time:this.repay.repayTime};Object(i.b)(t).then(function(t){e.TOSAST_STATE({text:t.msg}),t.errcode?2==t.errcode&&(e.REMOVE_USERINFO(),e.$router.push("/login")):(e.repayList.push({amount:e.repay.repayMoney,time:e.repay.repayTime}),e.repay.repayMoney="",e.repay.repayTime="")})}},addGoodsShow:function(){var e=this;this.dialogVisible=!0,this.goodsList.map(function(t){var s=e.stocks.indexOf(t.stock_name);s>-1&&e.stocks.splice(s,1)})},handleCheckedChange:function(){console.log(this.checkedStocks)},getStockList:function(){var e=this;Object(i.l)({username:this.userInfo.user,token:this.userInfo.token}).then(function(t){t.errcode?(e.TOSAST_STATE({text:t.msg}),2==t.errcode&&(e.REMOVE_USERINFO(),e.$router.push("/login"))):(e.stocks=t.data.list,console.log(e.stocks))})},onSubmitAddStock:function(){var e=this,t={username:this.userInfo.user,token:this.userInfo.token,customer_id:this.$route.params.id,checkedStocks:this.checkedStocks};Object(i.a)(t).then(function(t){console.log("addCusGoods",t),e.TOSAST_STATE({text:t.msg}),t.errcode||(t.data.list.map(function(t){e.goodsList.push({id:t.id,stock_amount:t.stock_amount,stock_num:t.stock_num,stock_price:t.stock_price,stock_name:t.stock_name})}),e.checkedStocks=[],e.dialogVisible=!1)})}}),created:function(){var e=this,t={params:{id:this.$route.params.id,token:this.userInfo.token,username:this.userInfo.user}};Object(i.h)(t).then(function(t){t.errcode?(e.TOSAST_STATE({text:t.msg}),2==t.errcode&&(e.REMOVE_USERINFO(),e.$router.push("/login"))):(e.form=t.data.info,e.goodsList=t.data.goods_list,e.repayList=t.data.repay_list)}),this.getStockList()}},u={render:function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",[s("Crumbs",{attrs:{crumbs1:"客户",crumbs2:"客户详情"}}),e._v(" "),s("div",{staticClass:"plugins-tips"},[e._v("客户基本信息")]),e._v(" "),s("div",{staticClass:"form-box"},[s("el-form",{ref:"rulesform",attrs:{"label-width":"100px",model:e.form,rules:e.rules}},[s("el-form-item",{attrs:{label:"姓名"}},[e._v(e._s(e.form.name))]),e._v(" "),s("el-form-item",{attrs:{label:"电话号码",prop:"tel"}},[s("el-input",{model:{value:e.form.tel,callback:function(t){e.$set(e.form,"tel",t)},expression:"form.tel"}})],1),e._v(" "),s("el-form-item",{attrs:{label:"住址",prop:"address"}},[s("el-input",{model:{value:e.form.address,callback:function(t){e.$set(e.form,"address",t)},expression:"form.address"}})],1),e._v(" "),s("el-form-item",{attrs:{label:"备注",prop:"remarks"}},[s("el-input",{attrs:{type:"textarea"},model:{value:e.form.remarks,callback:function(t){e.$set(e.form,"remarks",t)},expression:"form.remarks"}})],1),e._v(" "),s("el-form-item",[s("el-button",{attrs:{type:"primary"},on:{click:e.onSubmitCus}},[e._v("保存")])],1)],1)],1),e._v(" "),s("br"),e._v(" "),s("div",{staticClass:"plugins-tips"},[e._v("还款信息")]),e._v(" "),s("ul",{staticClass:"repay-info form-box"},[s("li",{staticClass:"amount"},[e._v("应还款总额： "),s("span",[e._v(e._s(e.currentAmount))]),e._v("元")]),e._v(" "),s("li",[e._m(0),e._v(" "),e._l(e.repayList,function(t,o){return s("ul",{key:o},[s("li",[e._v(e._s(t.amount))]),e._v(" "),s("li",[e._v(e._s(t.time))])])}),e._v(" "),s("ul",[s("li",[s("el-input",{attrs:{placeholder:"输入付款金额"},model:{value:e.repay.repayMoney,callback:function(t){e.$set(e.repay,"repayMoney",t)},expression:"repay.repayMoney"}})],1),e._v(" "),s("li",[s("el-date-picker",{staticStyle:{width:"100%"},attrs:{type:"date",placeholder:"选择日期","value-format":"yyyy-MM-dd"},model:{value:e.repay.repayTime,callback:function(t){e.$set(e.repay,"repayTime",t)},expression:"repay.repayTime"}})],1)]),e._v(" "),s("ul",[s("li",{staticClass:"add-btn"},[s("el-button",{attrs:{type:"primary"},on:{click:e.addRepay}},[e._v("添加")])],1)])],2)]),e._v(" "),s("div",{staticClass:"plugins-tips"},[e._v("客户用到的物料列表")]),e._v(" "),s("div",{staticClass:"form-box"},[s("el-form",[s("el-form-item",[s("el-table",{attrs:{data:e.goodsList}},[s("el-table-column",{attrs:{type:"index"}}),e._v(" "),s("el-table-column",{attrs:{prop:"stock_name",label:"名称"}}),e._v(" "),s("el-table-column",{attrs:{prop:"stock_num",label:"数量",width:"100"},scopedSlots:e._u([{key:"default",fn:function(t){return[s("el-input",{model:{value:t.row.stock_num,callback:function(s){e.$set(t.row,"stock_num",s)},expression:"scope.row.stock_num"}})]}}])}),e._v(" "),s("el-table-column",{attrs:{prop:"stock_price",label:"单价",width:"100"},scopedSlots:e._u([{key:"default",fn:function(t){return[s("el-input",{model:{value:t.row.stock_price,callback:function(s){e.$set(t.row,"stock_price",s)},expression:"scope.row.stock_price"}})]}}])}),e._v(" "),s("el-table-column",{attrs:{label:"金额",prop:"stock_amount"},scopedSlots:e._u([{key:"default",fn:function(t){return[e._v(e._s(e.perAmount)+"\n              "+e._s(t.row.stock_num*t.row.stock_price)+"\n            ")]}}])})],1)],1),e._v(" "),s("el-form-item",[s("el-button",{attrs:{type:"primary"},on:{click:e.onSubmitGoods}},[e._v("保存")]),e._v(" "),s("el-button",{attrs:{type:"text"},on:{click:e.addGoodsShow}},[e._v("添加物料")])],1)],1)],1),e._v(" "),e.dialogVisible?s("div",{staticClass:"addStock"},[s("h2",[e._v("添加物料")]),e._v(" "),s("el-form",[s("el-checkbox-group",{on:{change:e.handleCheckedChange},model:{value:e.checkedStocks,callback:function(t){e.checkedStocks=t},expression:"checkedStocks"}},e._l(e.stocks,function(t){return s("el-checkbox",{key:t,attrs:{label:t}},[e._v(e._s(t))])})),e._v(" "),s("el-form-item",[s("el-button",{attrs:{type:"primary"},on:{click:e.onSubmitAddStock}},[e._v("保存")])],1)],1)],1):e._e()],1)},staticRenderFns:[function(){var e=this.$createElement,t=this._self._c||e;return t("ul",[t("li",[this._v("付款金额(￥)")]),this._v(" "),t("li",[this._v("付款时间")])])}]};var l=s("VU/8")(c,u,!1,function(e){s("25KM")},"data-v-65350140",null);t.default=l.exports}});
//# sourceMappingURL=8.9d821f0e9b6f3e5221df.js.map