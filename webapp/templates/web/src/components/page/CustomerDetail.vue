<template>
  <div>
    <Crumbs crumbs1="客户" crumbs2="客户详情"></Crumbs>
    <div @click="download" class="download">下载客户详情</div>
    <!--<a href="files/list.xlsx" >下载客户详情</a>-->
    <div class="plugins-tips">客户基本信息</div>
    <div class="form-box">
      <el-form label-width="100px" :model="form" :rules="rules" ref="rulesform">
        <el-form-item label="姓名">{{form.name}}</el-form-item>
        <el-form-item label="电话号码" prop="tel">
          <el-input v-model="form.tel"></el-input>
        </el-form-item>
        <el-form-item label="住址" prop="address">
          <el-input v-model="form.address"></el-input>
        </el-form-item>
        <el-form-item label="备注" prop="remarks">
          <el-input type="textarea" v-model="form.remarks"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmitCus">保存</el-button>
        </el-form-item>
      </el-form>
    </div>
    <br>
    <div class="plugins-tips">还款信息</div>
    <ul class="repay-info form-box">
      <li class="amount">应还款总额： <span>{{currentAmount}}</span>元</li>
      <li>
        <ul>
          <li>付款金额(￥)</li>
          <li>付款时间</li>
        </ul>
        <ul v-for="(repay, i) in repayList" :key="i">
          <li>{{repay.amount}}</li>
          <li>{{repay.time}}</li>
        </ul>
        <ul>
          <li>
            <el-input v-model="repay.repayMoney" placeholder="输入付款金额"></el-input>
          </li>
          <li>
            <el-date-picker type="date" placeholder="选择日期"
                            v-model="repay.repayTime"
                            value-format="yyyy-MM-dd" style="width: 100%;"></el-date-picker>
          </li>
        </ul>
        <ul>
          <li class="add-btn">
            <el-button type="primary" @click="addRepay">添加</el-button>
          </li>
        </ul>

      </li>
    </ul>
    <div class="plugins-tips">客户用到的物料列表</div>
    <div class="form-box">
      <el-form>
        <el-form-item>
          <el-table :data="goodsList">
            <el-table-column type="index"></el-table-column>
            <el-table-column prop="stock_name" label="名称"></el-table-column>
            <el-table-column prop="stock_num" label="数量" width="100">
              <template slot-scope="scope">
                <el-input v-model="scope.row.stock_num"></el-input>
              </template>
            </el-table-column>
            <el-table-column prop="stock_price" label="单价" width="100">
              <template slot-scope="scope">
                <el-input v-model="scope.row.stock_price"></el-input>
              </template>
            </el-table-column>
            <el-table-column label="金额" prop="stock_amount">
              <template slot-scope="scope">{{perAmount}}
                {{scope.row.stock_num * scope.row.stock_price}}
              </template>
            </el-table-column>
          </el-table>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmitGoods">保存</el-button>
          <el-button type="text" @click="addGoodsShow">添加物料</el-button>
        </el-form-item>
      </el-form>

    </div>
    <div class="addStock" v-if="dialogVisible">
      <h2>添加物料</h2>
      <el-form>
        <el-checkbox-group v-model="checkedStocks" @change="handleCheckedChange">
          <el-checkbox v-for="stock in stocks" :label="stock" :key="stock">{{stock}}</el-checkbox>
        </el-checkbox-group>
        <el-form-item>
          <el-button type="primary" @click="onSubmitAddStock">保存</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
  import Crumbs from "../common/Crumbs.vue"
  import {
    getStocks,
    getCustomer,
    addCusRepay,
    updateCustomer,
    updateCusGoods,
    addCusGoods,
    exportCusDetail
  } from "../../api"
  import {mapMutations, mapState} from 'vuex'

  export default {
    components: {
      Crumbs
    },
    data() {
      return {
        form: {
          name: '',
          tel: '',
          remarks: '',
          address: ''
        },
        dialogVisible: false,
        rules: {
          name: [{required: true, message: '请输入客户姓名', trigger: 'blur'}],
          tel: [{required: true, message: '请输入电话号码', trigger: 'blur'}],
          address: [{required: true, message: '请输入客户住址', trigger: 'blur'}],
        },
        goodsList: [],
        stocks: [],
        checkedStocks: [],
        repay: {
          repayMoney: '',
          repayTime: ''
        },
        repayList: [],
      }
    },
    computed: {
      ...mapState(['userInfo']),
      // 总金额
      currentAmount() {
        let amount = 0
        this.goodsList.map(item => {
          amount += item.stock_price * item.stock_num
        })
        return amount
      },
      // 计算金额
      perAmount() {
        this.goodsList.map(item => {
          item.stock_price = +item.stock_price
          item.stock_num = +item.stock_num
          return item.stock_amount = item.stock_price * item.stock_num
        })
      }
    },
    methods: {
      ...mapMutations(['TOSAST_STATE', 'GET_USERINFO', 'REMOVE_USERINFO']),
      // 修改客户信息
      onSubmitCus() {
        this.$refs['rulesform'].validate((valid) => {
          if (valid) {
            let params = {
              token: this.userInfo.token,
              username: this.userInfo.user,
              id: this.$route.params.id,
              form: this.form
            }
            updateCustomer(params).then(res => {
              this.TOSAST_STATE({text: res.msg})
              if (res.errcode == 2) {
                this.REMOVE_USERINFO()
                this.$router.push('/login');
              }
            })
          } else {
            return false;
          }
        });
      },
      // 用料提交
      onSubmitGoods() {
        let params = {
          token: this.userInfo.token,
          username: this.userInfo.user,
          id: this.$route.params.id,
          goodsList: this.goodsList
        }
        updateCusGoods(params).then(res => {
          this.TOSAST_STATE({text: res.msg})
          if (res.errcode == 2) {
            this.REMOVE_USERINFO()
            this.$router.push('/login');
          }
        })
      },
      // 判断客户付款金额
      judgeRepayMoney() {
        if (this.repay.repayMoney) {
          return true
        } else {
          this.TOSAST_STATE({text: '请输入付款金额'})
          return false
        }
      },
      // 判断客户付款时间
      judgeRepayTime() {
        if (this.repay.repayTime) {
          return true
        } else {
          this.TOSAST_STATE({text: '请选择付款日期'})
          return false
        }
      },
      // 添加付款信息
      addRepay() {
        if (this.judgeRepayMoney() && this.judgeRepayTime()) {
          let param = {
            token: this.userInfo.token,
            username: this.userInfo.user,
            id: this.$route.params.id,
            amount: this.repay.repayMoney,
            time: this.repay.repayTime
          }
          addCusRepay(param).then(res => {
            this.TOSAST_STATE({text: res.msg})
            if (!res.errcode) {
              // 添加付款信息 提交
              this.repayList.push({amount: this.repay.repayMoney, time: this.repay.repayTime})
              this.repay.repayMoney = ''
              this.repay.repayTime = ''
            } else {
              if (res.errcode == 2) {
                this.REMOVE_USERINFO()
                this.$router.push('/login');
              }
            }
          })
        }
      },

      // 添加物料 内容显示
      addGoodsShow() {
        this.dialogVisible = true
        this.goodsList.map(item => {
          let index = this.stocks.indexOf(item.stock_name);
          if (index > -1) {
            this.stocks.splice(index, 1);
          }
        })
      },
      // 多选选择
      handleCheckedChange() {
        console.log(this.checkedStocks)
      },
      // 获取物料列表
      getStockList() {
        getStocks({username: this.userInfo.user, token: this.userInfo.token}).then(res => {
          if (!res.errcode) {
            this.stocks = res.data.list
          } else {
            this.TOSAST_STATE({text: res.msg})
            if (res.errcode == 2) {
              this.REMOVE_USERINFO()
              this.$router.push('/login');
            }
          }
        })
      },
      // 提交添加物料
      onSubmitAddStock() {
        let param = {
          username: this.userInfo.user,
          token: this.userInfo.token,
          customer_id: this.$route.params.id,
          checkedStocks: this.checkedStocks
        }
        addCusGoods(param).then(res => {
          this.TOSAST_STATE({text: res.msg})
          if (!res.errcode) {
            res.data.list.map(item => {
              this.goodsList.push({
                id: item.id,
                stock_amount: item.stock_amount,
                stock_num: item.stock_num,
                stock_price: item.stock_price,
                stock_name: item.stock_name
              })
            })
            this.checkedStocks = []
            this.dialogVisible = false
          }
        })
      },
      downloadFile(){
        var elemIF = document.createElement("iframe");
        elemIF.src = "files/list.xlsx";
        elemIF.style.display = "none";
        document.body.appendChild(elemIF);
      },
      download() {
        let param = {
          username: this.userInfo.user,
          token: this.userInfo.token,
          customer_id: this.$route.params.id
        }
        exportCusDetail(param).then(res => {
          if (!res.errcode) {
            this.downloadFile()
          }
        })
      }
    },
    created() {
      let param = {params: {id: this.$route.params.id, token: this.userInfo.token, username: this.userInfo.user}}
      getCustomer(param).then(res => {
        if (!res.errcode) {
          this.form = res.data.info
          this.goodsList = res.data.goods_list
          this.repayList = res.data.repay_list
        } else {
          this.TOSAST_STATE({text: res.msg})
          if (res.errcode == 2) {
            this.REMOVE_USERINFO()
            this.$router.push('/login');
          }
        }
      })
      this.getStockList()
    }
  }
</script>

<style scoped>
  ul, li {
    list-style: none;
  }
  .download {
    cursor: pointer;
    margin-bottom: 20px;
    color: #409eff;
    border: 1px solid #409eff;
    display: inline-block;
    padding: 10px;
    border-radius: 5px;
  }

  .repay-info {
    display: flex;
    align-items: center;
    border: 1px solid #ebeef5;
    margin-top: 20px;
    margin-bottom: 20px;
  }

  .amount {
    width: 200px;
  }

  .repay-info li {
    padding: 10px;
    width: 200px;
  }

  .repay-info > li:last-child {
    padding: 0;
    width: 400px;
  }

  .repay-info > li > ul {
    width: 100%;
    display: flex;
    border-bottom: 1px solid #ebeef5;
    text-align: center;
  }

  .repay-info > li > ul li {
    border-left: 1px solid #ebeef5;
  }

  .repay-info > li > ul:last-child {
    border-bottom: none;
  }

  .repay-info > li > ul li.add-btn {
    width: 100%;
  }

  .add-btn button {
    display: block;
    margin: 0 auto;
  }

  .addStock {
    position: fixed;
    left: 50%;
    top: 50%;
    width: 500px;
    height: 300px;
    background: #fff;
    border: 1px solid #eee;
    border-radius: 5px;
    margin-left: -250px;
    margin-top: -150px;
    padding: 10px;
    overflow: auto;
  }

  .addStock h2 {
    text-align: center;
    margin-bottom: 20px;
  }

  .el-checkbox + .el-checkbox {
    margin-left: 0;
  }

  .el-checkbox {
    margin: 0 30px 10px 0;
  }
</style>
