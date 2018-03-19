<template>
  <div>
    <Crumbs crumbs1="客户" crumbs2="客户列表"></Crumbs>
    <el-table :data="tableData">
      <el-table-column type="index"></el-table-column>
      <el-table-column prop="name" label="名称" min-width="100">
        <template slot-scope="scope">
          <router-link :to="/customer_list/+scope.row.id">{{scope.row.name}}</router-link>
        </template>
      </el-table-column>
      <el-table-column prop="tel" label="电话号码" width="120"></el-table-column>
      <el-table-column prop="address" label="住址" width="250"></el-table-column>
      <el-table-column prop="remarks" label="备注" width="200"></el-table-column>
    </el-table>
  </div>
</template>

<script>
  import Crumbs from "../common/Crumbs.vue"
  import {getCustomers} from "../../api"

  export default {
    components: {
      Crumbs
    },
    data(){
      return {
        tableData:[]
      }
    },
    created() {
      getCustomers().then(res => {
        if(!res.errcode) {
          this.tableData = res.data
        }
      })
    }
  }
</script>

<style scoped>
</style>
