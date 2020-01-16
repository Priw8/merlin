[title=MERLIN - about]
[Back to index](#s=MERLIN/doc/index)  

[include=MERLIN/README]
(ignore the above, it's there to the fact that this was pulled directly from the repo readme!)

Example ECL code created with MERLIN:  
[requireEclmap=17]
[code]
 void Boss() {
	[ins=512,17](0);
	[ins=400,17](0.0f, 128.0f);
	[ins=502,17](FLAG_INTANGIBLE);
	@effChargeGreen(3, 1);
	[ins=23,17](120);

	[ins=503,17](FLAG_INTANGIBLE);
	[ins=302,17](3);
	[ins=306,17](0, 0);
	[ins=500,17](56.0f, 56.0f);
	[ins=501,17](50.0f, 50.0f);
	@BossNon1();
	@stop();
 }

 void BossNon1() {
	[ins=511,17](9400);
	@setupNon();
	[ins=514,17](0, 1700, 2500, "BossCard1");
	[ins=527,17](0, 1700.0f, -24448);
	[ins=23,17](90);
	@BossNon1_at();
	@stop();
 }

 void BossNon1_at() {
	int et = 0;
	[ins=600,17](et);
	[ins=607,17](et, 3);
	[ins=605,17](et, 3.1f, 2.7f);
	@etExDist(et, 0);
	[ins=640,17](et, 2, "BossNon1_at2");

	int n = 0;
	while(1) {
		[ins=604,17](et, RANDRAD, 0.0f);
		[ins=606,17](et, 34, 2);
		@etExSpecialSet(et, 0, 2);

		if (n == 0) {
			[ins=606,17](et, 52, 2);
			[ins=602,17](et, ET_BUTTERFLY, COLOR8_GREEN);
			@etExBounceSet(et, 0, 1, 1, BOUNCE_U, NEGF);
			@etExAngleSet(et, 0, 2, 0, 1, ANGLE_RANDOM, 0.12f, NEGF);
		} else if (n == 1) {
			[ins=602,17](et, ET_BUTTERFLY, COLOR8_BLUE);
			@etExBounceSet(et, 0, 1, 1, BOUNCE_L, NEGF);
		} else if (n == 2) {
			[ins=602,17](et, ET_BUTTERFLY, COLOR8_PINK);
			@etExBounceSet(et, 0, 1, 1, BOUNCE_R, NEGF);
		}
		[ins=601,17](et);

		n += 1;
		if (n > 2)
			n = 0;
		[ins=23,17](70);
	}
 }

 void BossNon1_at2() {
	int et = 0;
	[ins=502,17](FLAG_INTANGIBLE);
	[ins=600,17](et);
	[ins=602,17](et, ET_SHARD, COLOR16_GREEN);
	[ins=606,17](et, 5, 1);
	[ins=607,17](et, 1);
	[ins=605,16]](et, 3.0f, 0.0f);
	[ins=604,17](et, rad(-90f) + (RANDF2*0.17f), 0.15f);
	@etExAccel(et, 0, 120, 0.06f, rad(90f));
	[ins=601,17](et);
 }
[/code]
[/requireEclmap]  

[Back to index](#s=MERLIN/doc/index)