webpackJsonp([8],{aeoA:function(t,e){},nj0Y:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=a("Dd8w"),r=a.n(n),o=a("D4TX"),l=a("gyMJ"),s=a("NYxO"),u={components:{Crumbs:o.a},data:function(){return{tableData:[],cur_page:1,perPage:20,dataSum:10}},created:function(){this.getData()},computed:r()({},Object(s.c)(["userInfo"])),methods:r()({},Object(s.b)(["TOSAST_STATE","GET_USERINFO","REMOVE_USERINFO"]),{handleCurrentChange:function(t){this.cur_page=t,this.getData()},getData:function(){var t=this;Object(l.l)({params:{username:this.userInfo.user,token:this.userInfo.token,result:!0,page:this.cur_page}}).then(function(e){e.errcode?(t.TOSAST_STATE({text:e.msg}),2==e.errcode&&(t.REMOVE_USERINFO(),t.$router.push("/login"))):(t.tableData=e.data.list,t.dataSum=e.data.count,t.perPage=e.data.perPage)})},deleteRow:function(t,e){var a=this;Object(l.d)({username:this.userInfo.user,token:this.userInfo.token,id:e.id}).then(function(e){e.errcode||a.tableData.splice(t,1),a.TOSAST_STATE({text:e.msg})})}})},c={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("Crumbs",{attrs:{crumbs1:"物料",crumbs2:"物料列表"}}),t._v(" "),a("el-table",{attrs:{data:t.tableData,"header-cell-style":{color:"#000"}}},[a("el-table-column",{attrs:{type:"index"}}),t._v(" "),a("el-table-column",{attrs:{prop:"name",label:"名称",width:"150"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("router-link",{attrs:{to:/stock_list/+e.row.id}},[t._v(t._s(e.row.name))])]}}])}),t._v(" "),a("el-table-column",{attrs:{prop:"unit",label:"单位",width:"50"}}),t._v(" "),a("el-table-column",{attrs:{prop:"price",label:"单价",width:"90"}}),t._v(" "),a("el-table-column",{attrs:{prop:"remarks",label:"备注"}}),t._v(" "),a("el-table-column",{attrs:{label:"操作",width:"80"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("el-button",{attrs:{type:"text",size:"small"},on:{click:function(a){t.deleteRow(e.$index,e.row)}}},[t._v("删除")])]}}])})],1),t._v(" "),a("div",{staticClass:"pagination"},[a("el-pagination",{attrs:{background:"",layout:"prev, pager, next",total:t.dataSum,"page-size":t.perPage},on:{"current-change":t.handleCurrentChange}})],1)],1)},staticRenderFns:[]};var i=a("VU/8")(u,c,!1,function(t){a("aeoA")},"data-v-3a7ef6ca",null);e.default=i.exports}});
//# sourceMappingURL=8.42f9925d16d02ebc8889.js.map