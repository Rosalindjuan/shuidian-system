webpackJsonp([7],{"+pyJ":function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var r=a("Dd8w"),n=a.n(r),u=a("D4TX"),s=a("gyMJ"),o=a("NYxO"),l={components:{Crumbs:u.a},data:function(){return{tableData:[],cur_page:1,perPage:10,dataSum:10}},computed:n()({},Object(o.c)(["userInfo"])),methods:n()({},Object(o.b)(["TOSAST_STATE","GET_USERINFO","REMOVE_USERINFO"]),{handleCurrentChange:function(t){this.cur_page=t,this.getData()},getData:function(){var t=this;Object(s.h)({token:this.userInfo.token,username:this.userInfo.user,result:!0,page:this.cur_page}).then(function(e){e.errcode?(t.TOSAST_STATE({text:e.msg}),2==e.errcode&&(t.REMOVE_USERINFO(),t.$router.push("/login"))):(t.tableData=e.data.list,t.dataSum=e.data.count,t.perPage=e.data.perPage)})}}),created:function(){this.getData()}},c={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("Crumbs",{attrs:{crumbs1:"客户",crumbs2:"客户列表"}}),t._v(" "),a("el-table",{attrs:{data:t.tableData}},[a("el-table-column",{attrs:{type:"index"}}),t._v(" "),a("el-table-column",{attrs:{prop:"name",label:"名称","min-width":"100"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("router-link",{attrs:{to:/customer_list/+e.row.id}},[t._v(t._s(e.row.name))])]}}])}),t._v(" "),a("el-table-column",{attrs:{prop:"tel",label:"电话号码",width:"120"}}),t._v(" "),a("el-table-column",{attrs:{prop:"address",label:"住址",width:"250"}}),t._v(" "),a("el-table-column",{attrs:{prop:"remarks",label:"备注",width:"200"}})],1),t._v(" "),a("div",{staticClass:"pagination"},[a("el-pagination",{attrs:{background:"",layout:"prev, pager, next",total:t.dataSum,"page-size":t.perPage},on:{"current-change":t.handleCurrentChange}})],1)],1)},staticRenderFns:[]};var i=a("VU/8")(l,c,!1,function(t){a("H4uh")},"data-v-68d136ac",null);e.default=i.exports},H4uh:function(t,e){}});
//# sourceMappingURL=7.063df35f9bfef27559df.js.map