<script setup lang="ts">
</script>

<template>
<p class="bg-blue-200 text-2xl p-4">Hello World!</p>
<div class="container mx-auto mt-4">
  <select class="select select-primary mb-4">
  <option disabled selected>性別は？</option>
  <option>男性</option>
  <option>女性</option>
  </select>
  <br>
  <select class="select select-primary mb-4">
    <option disabled selected>階級は？</option>
    <option>上層クラス（お金持ち）</option>
    <option>中級クラス（一般階級）</option>
    <option>下層クラス（労働階級）</option>
  </select>
  <br>
  <select class="select select-primary mb-4">
    <option disabled selected>年齢は？</option>
    <option v-for="i in [...Array(121).keys()]">
      {{ i }} 
     </option>
  </select> 歳
  <br>
+   <select class="select select-primary mb-4">
+     <option disabled selected>親・子の同伴者数は？</option>
+     <option v-for="i in [...Array(11).keys()]">
+       {{ i }} 
+     </option>
+   </select> 人
+   <br>
+   <select class="select select-primary mb-4">
+     <option disabled selected>兄弟姉妹の同伴者数は？</option>
+     <option v-for="i in [...Array(11).keys()]">
+       {{ i }} 
+     </option>
+   </select> 人
+   <br>
  <button class="btn btn-primary">結果を出力</button>
</div>
</template>