<template>
  <div>
    <Crumbs crumbs1="管理员" crumbs2="管理员列表"></Crumbs>
    <el-table :data="tableData">
      <el-table-column type="index"></el-table-column>
      <el-table-column prop="username" label="用户名">
        <template slot-scope="scope">
          <router-link :to="/admin_list/+scope.row.id">{{scope.row.username}}</router-link>
        </template>
      </el-table-column>
      <el-table-column prop="name" label="真实姓名" width="120"></el-table-column>
      <el-table-column prop="tel" label="电话号码" width="120">
        <template slot-scope="scope">
          {{scope.row.tel ? scope.row.tel : '----'}}
        </template>
      </el-table-column>
      <el-table-column prop="type" label="身份" width="120"></el-table-column>
      <el-table-column prop="is_active" label="有效性" width="80">
        <template slot-scope="scope">
          {{scope.row.is_active ? '有效' : '无效'}}
        </template>
      </el-table-column>
      <el-table-column label="操作" width="80px">
        <template slot-scope="scope">
          <el-button
            v-if="scope.row.type !='超级管理员'"
            @click="deleteRow(scope.$index, scope.row)" type="text" size="small">删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="pagination">
      <el-pagination
        background
        layout="prev, pager, next"
        :total="dataSum"
        :page-size="perPage"
        @current-change="handleCurrentChange">
      </el-pagination>
    </div>
  </div>
</template>

<script>
  import Crumbs from "../common/Crumbs.vue"
  import {getAdminList, deleteAdmin} from "../../api"
  import {mapMutations, mapState} from 'vuex'


  export default {
    components: {
      Crumbs
    },
    data() {
      return {
        tableData: [],
        cur_page: 1,
        perPage: 10,
        dataSum: 10
      }
    },
    methods: {
      ...mapMutations(['TOSAST_STATE']),
      // 删除一条数据
      deleteRow(index, row) {
        let userInfo = JSON.parse(localStorage.getItem('userInfo'));
        deleteAdmin({token: userInfo.token, username: userInfo.user, id: row.id}).then(res => {
          this.TOSAST_STATE({text: res.msg})
          if (!res.errcode) {
            this.tableData.splice(index, 1);
          } else {
            if (res.errcode == 2) {
              setTimeout(() => {
                localStorage.removeItem('userInfo')
                this.$router.push('/login');
              }, 1000)
            }
          }
        })
      },
      // 分页
      handleCurrentChange(val) {
        this.cur_page = val;
        this.getData();
      },
      // 获取数据
      getData() {
        let userInfo = JSON.parse(localStorage.getItem('userInfo'));
        getAdminList({
          params: {
            token: userInfo.token,
            username: userInfo.user,
            result: true,
            page: this.cur_page
          }
        }).then(res => {
          if (!res.errcode) {
            this.tableData = res.data.list;
            this.dataSum = res.data.count;
            this.perPage = res.data.perPage
          } else {
            this.TOSAST_STATE({text: res.msg})
            if (res.errcode == 2) {
              setTimeout(() => {
                localStorage.removeItem('userInfo')
                this.$router.push('/login');
              }, 1000)
            }
          }
        })
      },
    },
    created() {
      this.getData()
    }
  }
</script>

<style scoped>
</style>
