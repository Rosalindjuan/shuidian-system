<template>
  <div>
    <Crumbs crumbs1="物料" crumbs2="物料列表"></Crumbs>
    <!--操作 -->
    <!--<div class="handle-box">-->
    <!--<el-button type="primary" icon="delete" class="handle-del mr10">批量删除</el-button>-->
    <!--<el-input v-model="select_word" placeholder="筛选关键词" class="handle-input mr10"></el-input>-->
    <!--<el-button type="primary" icon="search">搜索</el-button>-->
    <!--</div>-->
    <!-- 列表 -->
    <el-table :data="tableData"
              :header-cell-style="{color: '#000'}">
      <el-table-column type="index"></el-table-column>
      <el-table-column prop="name" label="名称" width="150">
        <template slot-scope="scope">
          <router-link :to="/stock_list/+scope.row.id">{{scope.row.name}}</router-link>
        </template>
      </el-table-column>
      <!--<el-table-column prop="num" label="数量" text-align="center" width="80"></el-table-column>-->
      <el-table-column prop="unit" label="单位" width="50"></el-table-column>
      <!--<el-table-column prop="opening_price" label="进价" width="90"></el-table-column>-->
      <el-table-column prop="price" label="单价" width="90"></el-table-column>
      <!--<el-table-column prop="opening_amount" label="进价总金额" width="110"></el-table-column>-->
      <!--<el-table-column prop="amount" label="总金额" width="110"></el-table-column>-->
      <el-table-column prop="remarks" label="备注"></el-table-column>
      <el-table-column label="操作" width="80">
        <template slot-scope="scope">
          <el-button @click="deleteRow(scope.$index, scope.row)" type="text" size="small">删除</el-button>
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
  import {getStockList, newStock, deleteStock} from "../../api"
  import {mapMutations, mapState} from 'vuex'

  export default {
    components: {
      Crumbs
    },
    data() {
      return {
        tableData: [],
        cur_page: 1,
        perPage: 20,
        dataSum: 10
      }
    },
    created() {
      this.getData();
    },
    computed: {
      ...mapState(['userInfo'])
    },
    methods: {
      ...mapMutations(['TOSAST_STATE', 'GET_USERINFO', 'REMOVE_USERINFO']),
      // 分页
      handleCurrentChange(val) {
        this.cur_page = val;
        this.getData();
      },
      // 获取分页数据
      getData() {
        getStockList({
          params: {
            username: this.userInfo.user,
            token: this.userInfo.token,
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
              this.REMOVE_USERINFO()
              this.$router.push('/login');
            }
          }

        })
      },
      // 删除一条数据
      deleteRow(index, row) {
        deleteStock({username: this.userInfo.user, token: this.userInfo.token, id: row.id}).then(res => {
          if (!res.errcode) {
            this.tableData.splice(index, 1);
          }
          this.TOSAST_STATE({text: res.msg})
        })
      }
    }
  }
</script>

<style scoped>
  .handle-box {
    margin-bottom: 20px;
    min-width: 600px;
  }

  .handle-input {
    width: 300px;
    display: inline-block;
  }
</style>
