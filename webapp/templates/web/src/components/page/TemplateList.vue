<template>
  <div>
    <Crumbs crumbs1="模板" crumbs2="模板列表"></Crumbs>
    <el-table :data="tableData">
      <el-table-column type="index"></el-table-column>
      <el-table-column prop="name" label="名称">
        <template slot-scope="scope">
          <router-link :to="/template_list/+scope.row.id">{{scope.row.name}}</router-link>
        </template>
      </el-table-column>
      <el-table-column prop="remarks" label="备注"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button @click="deleteRow(scope.$index, scope.row)" type="text" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
  import Crumbs from "../common/Crumbs.vue"
  import {templateList, deleteTemplate} from "../../api"
  import {mapMutations, mapState} from 'vuex'


  export default {
    components: {
      Crumbs
    },
    data() {
      return {
        tableData: []
      }
    },
    methods: {
      ...mapMutations(['TOSAST_STATE']),
      // 获取数据
      getData() {
        let userInfo = JSON.parse(localStorage.getItem('userInfo'));
        templateList({token: userInfo.token, username: userInfo.user}).then(res => {
          if (!res.errcode) {
            this.tableData = res.data.list;
          }
        })
      },
      deleteRow(index, row) {
        let userInfo = JSON.parse(localStorage.getItem('userInfo'));
        deleteTemplate({token: userInfo.token, username: userInfo.user, id: row.id}).then(res => {
          this.TOSAST_STATE({text: res.msg})
          if (!res.errcode) {
            this.tableData.splice(index, 1);
          }
        })
      }
    },
    created() {
      this.getData();
    },
  }
</script>

<style scoped>
</style>
