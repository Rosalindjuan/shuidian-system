<template>
  <div class="wrap">
    <Crumbs crumbs1="库存" crumbs2="库存列表"></Crumbs>
    <!-- 操作 -->
    <!--<div class="handle-box">-->
      <!--<el-button type="primary" icon="delete" class="handle-del mr10">批量删除</el-button>-->
      <!--<el-input v-model="select_word" placeholder="筛选关键词" class="handle-input mr10"></el-input>-->
      <!--<el-button type="primary" icon="search">搜索</el-button>-->
    <!--</div>-->
    <br>
    <!-- 列表 -->
    <el-table :data="tableData" border>
      <el-table-column type="index"></el-table-column>
      <el-table-column prop="name" label="名称" width="150">
        <template slot-scope="scope">
          <router-link :to="/stock_list/+scope.row.id">{{scope.row.name}}</router-link>
        </template>
      </el-table-column>
      <el-table-column prop="num" label="数量" text-align="center" width="80"></el-table-column>
      <el-table-column prop="unit" label="单位" width="50"></el-table-column>
      <el-table-column prop="opening_price" label="进价" width="90"></el-table-column>
      <el-table-column prop="price" label="单价" width="90"></el-table-column>
      <el-table-column prop="opening_amount" label="进价总金额" width="110"></el-table-column>
      <el-table-column prop="amount" label="总金额" width="110"></el-table-column>
      <el-table-column prop="remarks" label="备注" width="200"></el-table-column>
      <el-table-column prop="remarks" label="操作" width="80">
        <template slot-scope="scope">
          <el-button @click="deleteRow(scope.$index, scope.row)" type="text" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="pagination">
      <el-pagination
        background
        layout="prev, pager, next"
        :page-size="10"
        :total="tableData.length">
      </el-pagination>
    </div>
  </div>
</template>

<script>
  import Crumbs from "../common/Crumbs.vue"
  import {getStockList, newStock, deleteStock} from "../../api"
  export default {
    components: {
      Crumbs
    },
    data() {
      return {
        tableData: [],
        cur_page: 1,
        multipleSelection: [],
        select_cate: '',
        select_word: '',
        del_list: [],
        is_search: false
      }
    },
    created() {
      this.getData();
    },
    computed: {
//      data() {
//        const self = this;
//        return self.tableData.filter(function (d) {
//          let is_del = false;
//          for (let i = 0; i < self.del_list.length; i++) {
//            if (d.name === self.del_list[i].name) {
//              is_del = true;
//              break;
//            }
//          }
//          if (!is_del) {
//            if (d.address.indexOf(self.select_cate) > -1 &&
//              (d.name.indexOf(self.select_word) > -1 ||
//                d.address.indexOf(self.select_word) > -1)
//            ) {
//              return d;
//            }
//          }
//        })
//      }
    },
    methods: {
      handleCurrentChange(val) {
        this.cur_page = val;
//        this.getData();
      },
      getData() {
        getStockList({params:{result: true, page: this.cur_page}}).then(res => {
          this.tableData = res.data.list;
        })
      },
      deleteRow(index, row) {
        deleteStock({id: row.id}).then(res => {
          if(!res.errcode) {
            this.tableData.splice(index, 1);
          }
          alert(res.msg)
        })
      },
//      search() {
//        this.is_search = true;
//      },
//      formatter(row, column) {
//        return row.address;
//      },
//      filterTag(value, row) {
//        return row.tag === value;
//      },
//      delAll() {
//        const self = this,
//          length = self.multipleSelection.length;
//        let str = '';
//        self.del_list = self.del_list.concat(self.multipleSelection);
//        for (let i = 0; i < length; i++) {
//          str += self.multipleSelection[i].name + ' ';
//        }
//        self.$message.error('删除了' + str);
//        self.multipleSelection = [];
//      },
//      handleSelectionChange(val) {
//        this.multipleSelection = val;
//      }
    }
  }
</script>

<style scoped>
  .handle-box{
    margin-bottom: 20px;
    min-width: 600px;
  }

  .handle-input{
    width: 300px;
    display: inline-block;
  }
</style>
