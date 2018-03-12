<template>
  <div>
    <Crumbs crumbs1="模板" crumbs2="模板列表"></Crumbs>
    <el-table :data="tableData">
      <el-table-column type="index"></el-table-column>
      <el-table-column prop="name" label="名称" width="150">
        <template slot-scope="scope">
          <router-link :to="/template_list/+scope.row.id">{{scope.row.name}}</router-link>
        </template>
      </el-table-column>
      <el-table-column prop="remarks" label="备注" width="200"></el-table-column>
      <el-table-column label="操作" width="80">
        <template slot-scope="scope">
          <el-button @click="deleteRow(scope.$index, scope.row)" type="text" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
  import Crumbs from "../common/Crumbs.vue"
  import {templateList} from "../../api"


  export default {
    components: {
      Crumbs
    },
    data(){
      return {
        tableData: []
      }
    },
    methods: {
      getData() {
        templateList().then(res => {
          console.log(res)
          if(!res.errcode) {
            this.tableData = res.data.list;
          }
        })
      },
      deleteRow(index, row) {
//        deleteStock({id: row.id}).then(res => {
//          if(!res.errcode) {
//            this.tableData.splice(index, 1);
//          }
//          alert(res.msg)
//        })
      }
    },
    created() {
      this.getData();
    },
  }
</script>

<style scoped>
</style>
