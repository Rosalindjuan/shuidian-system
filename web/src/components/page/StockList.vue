<template>
  <div>
    <Crumbs crumbs1="库存" crumbs2="库存列表"></Crumbs>
    <!-- 操作 -->
    <div class="handle-box">
      <el-button type="primary" icon="delete" class="handle-del mr10">批量删除</el-button>
      <el-select v-model="select_cate" placeholder="筛选省份" class="handle-select mr10">
        <el-option key="1" label="广东省" value="广东省"></el-option>
        <el-option key="2" label="湖南省" value="湖南省"></el-option>
      </el-select>
      <el-input v-model="select_word" placeholder="筛选关键词" class="handle-input mr10"></el-input>
      <el-button type="primary" icon="search">搜索</el-button>
    </div>
    <br>
    <!-- 列表 -->
    <el-table :data="tableData" border>
      <el-table-column type="index"></el-table-column>
      <el-table-column prop="name" label="名称" width="150"></el-table-column>
      <el-table-column prop="num" label="数量" text-align="center" width="80"></el-table-column>
      <el-table-column prop="unit" label="单位" width="50"></el-table-column>
      <el-table-column prop="opening_price" label="进价" width="100"></el-table-column>
      <el-table-column prop="price" label="单价" width="100"></el-table-column>
      <el-table-column prop="opening_amount" label="进价总金额" width="120"></el-table-column>
      <el-table-column prop="amount" label="总金额" width="120"></el-table-column>
      <el-table-column prop="remark" label="备注" width="150"></el-table-column>
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
  export default {
    components: {
      Crumbs
    },
    data() {
      return {
        tableData: [{
          name: "林丽1",
          num: 2,
          unit: '个',
          opening_price: 40,
          price: 80,
          opening_amount: 140,
          amount: 160,
          remark: "吉林省 辽源市 龙山区"
        }, {
          name: "林丽2",
          num: 2,
          unit: '个',
          opening_price: 40,
          price: 80,
          opening_amount: 140,
          amount: 160,
          remark: "吉林省 辽源市 龙山区"
        }, {
          name: "林丽3",
          num: 2,
          unit: '个',
          opening_price: 40,
          price: 80,
          opening_amount: 140,
          amount: 160,
          remark: "吉林省 辽源市 龙山区"
        }, {
          name: "林丽4",
          num: 2,
          unit: '个',
          opening_price: 40,
          price: 80,
          opening_amount: 140,
          amount: 160,
          remark: "吉林省 辽源市 龙山区"
        }, {
          name: "林丽5",
          num: 2,
          unit: '个',
          opening_price: 40,
          price: 80,
          opening_amount: 140,
          amount: 160,
          remark: "吉林省 辽源市 龙山区"
        },{
          name: "林丽1",
          num: 2,
          unit: '个',
          opening_price: 40,
          price: 80,
          opening_amount: 140,
          amount: 160,
          remark: "吉林省 辽源市 龙山区"
        },],
        cur_page: 1,
        multipleSelection: [],
        select_cate: '',
        select_word: '',
        del_list: [],
        is_search: false
      }
    },
    created() {
//      this.getData();
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
//      getData() {
//        this.tableData = [
//          {
//          name: "林丽1",
//          num: 2,
//          unit: '个',
//          opening_price: 40,
//          price: 80,
//          opening_amount: 140,
//          amount: 160,
//          remark: "吉林省 辽源市 龙山区"
//        }, {
//          name: "林丽2",
//          num: 2,
//          unit: '个',
//          opening_price: 40,
//          price: 80,
//          opening_amount: 140,
//          amount: 160,
//          remark: "吉林省 辽源市 龙山区"
//        }]
////        let self = this;
////        if (process.env.NODE_ENV === 'development') {
////          self.url = '/ms/table/list';
////        }
////        ;
////        self.$axios.post(self.url, {page: self.cur_page}).then((res) => {
////          self.tableData = res.data.list;
////        })
//      },
//      search() {
//        this.is_search = true;
//      },
//      formatter(row, column) {
//        return row.address;
//      },
//      filterTag(value, row) {
//        return row.tag === value;
//      },
//      handleEdit(index, row) {
//        this.$message('编辑第' + (index + 1) + '行');
//      },
//      handleDelete(index, row) {
//        this.$message.error('删除第' + (index + 1) + '行');
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
  }
  .handle-select{
    width: 120px;
  }
  .handle-input{
    width: 300px;
    display: inline-block;
  }
</style>
