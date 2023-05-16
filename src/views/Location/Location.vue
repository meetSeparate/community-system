<!-- vue 3 引入百度api -->
<template>
  <div id="allmap"></div>
</template>

<script>
import {defineComponent, nextTick, onMounted} from "vue";

export default defineComponent({
  setup() {
    onMounted(() => {
      nextTick(() => {
        initMap();
      });
    });
    const initMap = () => {
      let Bmap = window.BMap;
      let map = new Bmap.Map("allmap");
      map.centerAndZoom(new Bmap.Point(104.04263635868074, 30.556100647961866), 11);
      map.enableScrollWheelZoom(true);
      let geolocation = new Bmap.Geolocation();
      geolocation.getCurrentPosition(function (r) {
        if (this.getStatus() == BMAP_STATUS_SUCCESS) {
          var mk = new Bmap.Marker(r.point);
          map.addOverlay(mk);
          map.panTo(r.point);
          var p1 = new Bmap.Point(r.point.lng, r.point.lat);
          var p2 = new Bmap.Point(r.point.lng - 0.0200, r.point.lat - 0.0200);

          var driving = new Bmap.DrivingRoute(map, {renderOptions: {map: map, autoViewport: true}});
          driving.search(p1, p2);
        } else {
          alert('failed' + this.getStatus());
        }
      });
    };
    return {};
  },
});

</script>
<style scoped>
#allmap {
  width: 100%;
  height: 580px;
}
</style>